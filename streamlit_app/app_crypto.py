import streamlit as st
import boto3
import pandas as pd
import io
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Crypto Analytics", page_icon="B", layout="wide")

BUCKET = "crypto-bigdata-2026"
COLORS = {
    'Bitcoin': '#f7931a', 'Ethereum': '#627eea',
    'Solana': '#14f195', 'Cardano': '#4a90d9', 'Chainlink': '#375bd2'
}

@st.cache_data
def load_data():
    s3 = boto3.client('s3', region_name='us-east-1')
    paginator = s3.get_paginator('list_objects_v2')
    dfs = []
    for page in paginator.paginate(Bucket=BUCKET, Prefix='trusted/crypto_prices/'):
        for obj in page.get('Contents', []):
            key = obj['Key']
            if key.endswith('.csv') and 'Name=' in key:
                coin_name = key.split('Name=')[1].split('/')[0]
                response = s3.get_object(Bucket=BUCKET, Key=key)
                try:
                    df_tmp = pd.read_csv(io.BytesIO(response['Body'].read()))
                    df_tmp['Name'] = coin_name
                    dfs.append(df_tmp)
                except:
                    pass
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

with st.spinner('Cargando datos desde S3...'):
    df = load_data()
    if not df.empty:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        for c in ['Close','Open','High','Low','Volume','daily_return','volatility']:
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors='coerce')

st.title("Crypto Analytics Dashboard")
st.caption("ST0263 Proyecto Big Data EAFIT 2026 | Bitcoin · Ethereum · Solana · Cardano · Chainlink")

if df.empty:
    st.error("No se pudieron cargar los datos desde S3.")
    st.stop()

cols = st.columns(5)
for i, (coin, color) in enumerate(COLORS.items()):
    df_coin = df[df['Name'] == coin]
    if not df_coin.empty:
        last = df_coin['Close'].dropna().iloc[-1]
        cols[i].metric(coin, f"${last:,.2f}")

st.divider()

st.subheader("P4 - Evolucion del precio mensual (BTC · ETH · SOL)")
df_e = df[df['Name'].isin(['Bitcoin','Ethereum','Solana'])].dropna(subset=['Date','Close'])
fig4 = px.line(df_e, x='Date', y='Close', color='Name',
               color_discrete_map=COLORS, template='plotly_dark',
               labels={'Close':'Precio (USD)', 'Date':'Fecha'})
st.plotly_chart(fig4, use_container_width=True)

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("P2 - Volatilidad por moneda")
    vol = df.groupby('Name')['volatility'].mean().reset_index()
    vol.columns = ['Name','volatilidad_pct']
    vol = vol.sort_values('volatilidad_pct')
    fig2 = px.bar(vol, x='volatilidad_pct', y='Name', orientation='h',
                  color='Name', color_discrete_map=COLORS, template='plotly_dark')
    fig2.update_layout(showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

with col_b:
    st.subheader("P5 - Rendimiento promedio por mes")
    rend = df.groupby('Month')['daily_return'].mean().reset_index()
    meses = {1:'Ene',2:'Feb',3:'Mar',4:'Abr',5:'May',6:'Jun',
             7:'Jul',8:'Ago',9:'Sep',10:'Oct',11:'Nov',12:'Dic'}
    rend['mes'] = rend['Month'].map(meses)
    rend['color'] = rend['daily_return'].apply(
        lambda x: '#10b981' if x >= 0 else '#ef4444')
    fig5 = go.Figure(go.Bar(
        x=rend['mes'], y=rend['daily_return'],
        marker_color=rend['color']))
    fig5.update_layout(template='plotly_dark', showlegend=False,
                       yaxis_title='Rendimiento (%)')
    st.plotly_chart(fig5, use_container_width=True)

st.subheader("P3 - Correlacion Volumen vs Precio de cierre")
coin_sel = st.selectbox('Selecciona la moneda', list(COLORS.keys()))
df_sel = df[df['Name'] == coin_sel].dropna(subset=['Volume','Close'])
corr_val = df_sel['Volume'].corr(df_sel['Close'])
fig3 = px.scatter(df_sel, x='Volume', y='Close',
                  trendline='ols', hover_data=['Date'],
                  color_discrete_sequence=[COLORS[coin_sel]],
                  template='plotly_dark',
                  title=f'Volumen vs Precio - {coin_sel}')
st.plotly_chart(fig3, use_container_width=True)
st.info(f"Correlacion de Pearson ({coin_sel}): r = {corr_val:.4f}")
