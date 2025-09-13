PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- Tabla de países
CREATE TABLE paiss (
    id INTEGER NOT NULL,
    nombre_pais VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Tabla de mundiales
CREATE TABLE mundial (
    id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    pais_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(pais_id) REFERENCES paiss(id)
);

-- Índices
CREATE INDEX ix_paiss_id ON paiss (id);
CREATE INDEX ix_mundial_id ON mundial (id);

-- Datos de ejemplo
INSERT INTO paiss (id, nombre_pais) VALUES
(1, 'Argentina'),
(2, 'Brasil'),
(3, 'Alemania'),
(4, 'Francia');

INSERT INTO mundial (id, title, pais_id) VALUES
(1, 'Qatar 2022', 1),      -- Argentina
(2, 'Brasil 2014', 3),     -- Alemania
(3, 'Rusia 2018', 4),      -- Francia
(4, 'Corea-Japon 2002', 2);-- Brasil

COMMIT;
