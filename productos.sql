-- Base de datos y tabla de ejemplo para MySQL o MariaDB.
CREATE DATABASE IF NOT EXISTS tienda_escolar
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE tienda_escolar;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    existencias INT NOT NULL
);

INSERT INTO productos (nombre, precio, existencias) VALUES
    ('Cuaderno profesional', 45.50, 20),
    ('Lapiz', 8.00, 50),
    ('Borrador', 6.50, 35),
    ('Regla de 30 cm', 18.90, 15),
    ('Mochila escolar', 399.00, 8);
