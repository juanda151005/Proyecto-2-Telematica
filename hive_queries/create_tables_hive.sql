-- Punto 5: Catalogación con Hive en EMR/Hue
-- Hue: http://98.93.38.193:8888

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS cryptodb;
USE cryptodb;

-- Tabla de precios históricos (particionada por Name)
CREATE EXTERNAL TABLE IF NOT EXISTS cryptodb.crypto_prices (
    SNo INT, Name STRING, Symbol STRING, fecha STRING,
    High DOUBLE, Low DOUBLE, Open DOUBLE, Close DOUBLE,
    Volume DOUBLE, Marketcap DOUBLE, Year INT, Month INT,
    daily_return DOUBLE, volatility DOUBLE
)
PARTITIONED BY (Name_part STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://crypto-bigdata-2026/trusted/crypto_prices/'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Agregar particiones manualmente
ALTER TABLE cryptodb.crypto_prices ADD PARTITION (Name_part='Bitcoin')
LOCATION 's3://crypto-bigdata-2026/trusted/crypto_prices/Name=Bitcoin/';
ALTER TABLE cryptodb.crypto_prices ADD PARTITION (Name_part='Ethereum')
LOCATION 's3://crypto-bigdata-2026/trusted/crypto_prices/Name=Ethereum/';
ALTER TABLE cryptodb.crypto_prices ADD PARTITION (Name_part='Solana')
LOCATION 's3://crypto-bigdata-2026/trusted/crypto_prices/Name=Solana/';
ALTER TABLE cryptodb.crypto_prices ADD PARTITION (Name_part='Cardano')
LOCATION 's3://crypto-bigdata-2026/trusted/crypto_prices/Name=Cardano/';
ALTER TABLE cryptodb.crypto_prices ADD PARTITION (Name_part='Chainlink')
LOCATION 's3://crypto-bigdata-2026/trusted/crypto_prices/Name=Chainlink/';

-- Tabla de metadata
CREATE EXTERNAL TABLE IF NOT EXISTS cryptodb.coins_metadata (
    id INT, symbol STRING, name STRING, category STRING,
    blockchain STRING, launch_year INT, max_supply BIGINT,
    consensus STRING, coingecko_id STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://crypto-bigdata-2026/trusted/coins_metadata/'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Verificar
SHOW TABLES IN cryptodb;
