-- Punto 6: Consultas SQL en Amazon Athena
-- Database: cryptodb_trusted

-- P1: Crecimiento porcentual anual por moneda (2020-2024)
SELECT 
    Name,
    Year,
    ROUND(((MAX(Close) - MIN(Close)) / MIN(Close)) * 100, 2) AS crecimiento_pct
FROM crypto_prices
WHERE Year BETWEEN 2020 AND 2024
GROUP BY Name, Year
ORDER BY Year, crecimiento_pct DESC;

-- P2: Volatilidad historica por moneda
SELECT
    Name,
    ROUND(AVG((High - Low) / Close * 100), 3) AS volatilidad_pct
FROM crypto_prices
GROUP BY Name
ORDER BY volatilidad_pct DESC;

-- P3: Estadisticas de volumen y precio por moneda
SELECT
    Name,
    ROUND(AVG(CAST(Volume AS DOUBLE)), 0) AS volumen_promedio,
    ROUND(AVG(CAST(Close AS DOUBLE)), 2) AS precio_promedio,
    ROUND(MIN(CAST(Close AS DOUBLE)), 2) AS precio_minimo,
    ROUND(MAX(CAST(Close AS DOUBLE)), 2) AS precio_maximo,
    COUNT(*) AS dias
FROM crypto_prices
GROUP BY Name
ORDER BY precio_promedio DESC;

-- P4: Evolucion precio mensual BTC, ETH, SOL (2020-2024)
SELECT
    Name,
    Year,
    Month,
    ROUND(AVG(CAST(Close AS DOUBLE)), 2) AS precio_promedio
FROM crypto_prices
WHERE Name IN ('Bitcoin', 'Ethereum', 'Solana')
  AND CAST(Year AS INT) BETWEEN 2020 AND 2024
GROUP BY Name, Year, Month
ORDER BY Name, Year, Month;

-- P5: Rendimiento promedio por mes del año
SELECT
    Month,
    ROUND(AVG(CAST(daily_return AS DOUBLE)), 4) AS rendimiento_pct,
    COUNT(*) AS dias_muestra
FROM crypto_prices
GROUP BY Month
ORDER BY Month;
