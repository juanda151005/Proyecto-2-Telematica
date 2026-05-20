-- Tablas creadas via Glue Crawler en database: cryptodb_trusted
-- Crawler: crawler-crypto-trusted
-- Data source: s3://crypto-bigdata-2026/trusted/

-- Tabla 1: crypto_prices (particionada por Name)
-- Columnas: SNo, Name, Symbol, Date, High, Low, Open, 
--           Close, Volume, Marketcap, Year, Month,
--           daily_return, volatility

-- Tabla 2: coins_metadata
-- Columnas: id, symbol, name, category, blockchain,
--           launch_year, max_supply, consensus, coingecko_id

-- Verificacion en Athena:
SELECT Name, COUNT(*) as filas
FROM crypto_prices
GROUP BY Name
ORDER BY Name;

SELECT * FROM coins_metadata;
