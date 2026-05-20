# Punto 3 — Ingesta automática a S3

## Descripción
Script Python que ingesta automáticamente las 3 fuentes de datos hacia el
datalake en S3 en las zonas correctas.

## Bucket S3
crypto-bigdata-2026

## Estructura S3
- raw/csv/     — 5 CSV históricos de Kaggle (coin_Bitcoin.csv, etc.)
- raw/api/     — Datos en tiempo real de CoinGecko API
- raw/rds/     — Export de tabla coins_metadata de MariaDB RDS

## Ejecución
pip3 install boto3 requests pandas pymysql
python3 ingest_crypto.py

## Fuentes ingestadas
1. Kaggle CSV — 5 archivos de precios históricos
2. CoinGecko API — precios y métricas actualizadas
3. RDS MariaDB — tabla coins_metadata (5 registros)
