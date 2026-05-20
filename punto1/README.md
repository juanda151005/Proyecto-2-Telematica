# Punto 1 — Caso de estudio

## Tema
Análisis del comportamiento histórico de criptomonedas y tendencias del mercado crypto.

## Descripción
Este caso de estudio analiza el comportamiento histórico de Bitcoin (BTC),
Ethereum (ETH), Solana (SOL), Cardano (ADA) y Chainlink (LINK) usando precios
diarios, volúmenes de transacción y variaciones de mercado entre 2017 y 2024.
El objetivo es identificar tendencias, comparar rendimiento entre activos y
responder preguntas de negocio sobre volatilidad, crecimiento y estacionalidad.

## Fuentes de datos

### Fuente 1 (Archivo - CSV)
Dataset histórico de criptomonedas descargado desde Kaggle.
URL: https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory

### Fuente 2 (URL/API)
API pública de CoinGecko — precios y métricas actualizadas, sin API key.
URL: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,solana,cardano,chainlink

### Fuente 3 (Base de datos)
Tabla coins_metadata en MariaDB/RDS con información descriptiva de cada criptomoneda.

## Preguntas de negocio

- P1: ¿Cuáles fueron las criptomonedas con mayor crecimiento porcentual anual (2020-2024)?
- P2: ¿Qué criptomoneda ha presentado mayor volatilidad histórica medida como AVG((High-Low)/Close) por mes?
- P3: ¿Existe correlación entre el volumen de transacciones y el precio de cierre de cada criptomoneda?
- P4: ¿Cómo ha evolucionado el precio promedio mensual de Bitcoin, Ethereum y Solana entre 2020 y 2024?
- P5: ¿Qué meses del año presentan mayor rendimiento promedio en el mercado crypto medido como (Close-Open)/Open?
