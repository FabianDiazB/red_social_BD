
CREATE OR REPLACE FUNCTION get_user
(
    p_user_username TEXT,
    p_user_password TEXT
)
RETURNS TABLE
(id INTEGER, username VARCHAR, email VARCHAR, password VARCHAR,rol VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM usuarios
    WHERE usuarios.username = p_user_username AND usuarios.password = p_user_password;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION insertar_publicacion_viaje
(id_usuario INTEGER, contenido TEXT, enlace TEXT )
RETURNS VOID AS $$
BEGIN
    INSERT INTO publicaciones
        (usuario_id, publicacion,links)
    VALUES
        (id_usuario, contenido, enlace);
END;
$$ LANGUAGE plpgsql;



INSERT INTO usuarios
    (username, email, password, rol)
VALUES
    ('admin', 'admin@gmail', 'admin', 'admin'),
    ('juanperez', 'jperez@tec.cr', 'passwordjuan', 'editor'),
    ('mariacastro', 'mcastro@tec.cr', 'passwordmaria', 'editor'),
    ('joserodriguez', 'jrodriguez@tec.cr', 'passwordjose', 'lector'),
    ('carlagonzalez', 'cgonzalez@tec.cr', 'passwordcarla', 'lector'),
    ('luisfernandez', 'lfernandez@tec.cr', 'passwordluis', 'editor'),
    ('alejandramora', 'amora@tec.cr', 'passwordalejandra', 'editor');

