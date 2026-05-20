CREATE DATABASE IF NOT EXISTS cryptodb;
USE cryptodb;

CREATE TABLE coins_metadata (
    id           INT PRIMARY KEY AUTO_INCREMENT,
    symbol       VARCHAR(10)  NOT NULL,
    name         VARCHAR(50)  NOT NULL,
    category     VARCHAR(50),
    blockchain   VARCHAR(50),
    launch_year  INT,
    max_supply   BIGINT,
    consensus    VARCHAR(30),
    coingecko_id VARCHAR(30)
);

INSERT INTO coins_metadata
  (symbol, name, category, blockchain, launch_year, max_supply, consensus, coingecko_id)
VALUES
  ('BTC',  'Bitcoin',   'Store of Value',  'Bitcoin',  2009, 21000000,    'Proof of Work',    'bitcoin'),
  ('ETH',  'Ethereum',  'Smart Contracts', 'Ethereum', 2015, NULL,        'Proof of Stake',   'ethereum'),
  ('SOL',  'Solana',    'Smart Contracts', 'Solana',   2020, NULL,        'Proof of History', 'solana'),
  ('ADA',  'Cardano',   'Smart Contracts', 'Cardano',  2017, 45000000000, 'Proof of Stake',   'cardano'),
  ('LINK', 'Chainlink', 'Oracle Network',  'Ethereum', 2017, 1000000000,  'PoS/Oracle',       'chainlink');

SELECT * FROM coins_metadata;
