import boto3
import requests
import pandas as pd
import pymysql
import io
from datetime import datetime

BUCKET   = "crypto-bigdata-2026"
RDS_HOST = "cryptodb.c8gnxtkwuinq.us-east-1.rds.amazonaws.com"
RDS_USER = "admin"
RDS_PASS = "crypto2026"
RDS_DB   = "cryptodb"
HOY      = datetime.now().strftime("%Y%m%d")

s3 = boto3.client('s3', region_name='us-east-1')

def ingest_kaggle_csvs():
    print("[1/3] Subiendo CSVs de Kaggle...")
    coins = ['Bitcoin','Ethereum','Solana','Cardano','Chainlink']
    for coin in coins:
        local = f"/home/ec2-user/coin_{coin}.csv"
        key   = f"raw/csv/coin_{coin}.csv"
        s3.upload_file(local, BUCKET, key)
        print(f"  OK coin_{coin}.csv subido")

def ingest_coingecko():
    print("[2/3] Descargando de CoinGecko API...")
    url = ("https://api.coingecko.com/api/v3/coins/markets"
           "?vs_currency=usd"
           "&ids=bitcoin,ethereum,solana,cardano,chainlink"
           "&order=market_cap_desc&per_page=10&sparkline=false")
    data = requests.get(url, timeout=15).json()
    rows = [{
        'symbol':        c['symbol'].upper(),
        'name':          c['name'],
        'current_price': c['current_price'],
        'market_cap':    c['market_cap'],
        'total_volume':  c['total_volume'],
        'high_24h':      c['high_24h'],
        'low_24h':       c['low_24h'],
        'change_24h_pct':c['price_change_percentage_24h'],
        'ath':           c['ath'],
        'fetch_date':    HOY
    } for c in data]
    buf = io.StringIO()
    pd.DataFrame(rows).to_csv(buf, index=False)
    s3.put_object(Bucket=BUCKET, Key=f"raw/api/coingecko_{HOY}.csv", Body=buf.getvalue())
    print(f"  OK coingecko_{HOY}.csv subido ({len(rows)} monedas)")

def ingest_rds():
    print("[3/3] Exportando RDS MariaDB...")
    conn = pymysql.connect(
        host=RDS_HOST, user=RDS_USER,
        password=RDS_PASS, database=RDS_DB,
        ssl={'ssl': True}
    )
    df = pd.read_sql("SELECT * FROM coins_metadata", conn)
    conn.close()
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    s3.put_object(Bucket=BUCKET, Key="raw/rds/coins_metadata.csv", Body=buf.getvalue())
    print(f"  OK coins_metadata.csv subido ({len(df)} filas)")

if __name__ == "__main__":
    ingest_kaggle_csvs()
    ingest_coingecko()
    ingest_rds()
    print("\nIngesta completa.")
