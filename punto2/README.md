# Punto 2 — Base de datos RDS MariaDB

## Configuración
- Motor: MariaDB 11.8.6 en Amazon RDS
- Instancia: db.t4g.micro
- Base de datos: cryptodb
- Tabla: coins_metadata (5 registros)
- Endpoint: cryptodb.c8gnxtkwuinq.us-east-1.rds.amazonaws.com
- Puerto: 3306

## Tabla coins_metadata
Contiene información descriptiva de cada criptomoneda:
id, symbol, name, category, blockchain, launch_year, max_supply, consensus, coingecko_id

## Monedas
- BTC — Bitcoin — Store of Value
- ETH — Ethereum — Smart Contracts
- SOL — Solana — Smart Contracts
- ADA — Cardano — Smart Contracts
- LINK — Chainlink — Oracle Network
