-- Usuarios
CREATE TABLE usuarios
(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Viajes
CREATE TABLE publicacion_viajes
(
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(100),
    usuario_id INT REFERENCES usuarios(id),
    links TEXT

);
