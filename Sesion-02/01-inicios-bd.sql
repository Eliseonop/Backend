CREATE database  pruebas;

USE pruebas;
-- https://dev.mysql.com/doc/refman/8.0/en/data-types.html


CREATE TABLE personas(
	-- Ahora definimos las columnas pertenecientes a esta tabla
    id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,  --  se podra almacenar caracteres como maximo 100
    dni CHAR(8) NOT NULL, -- se podra almacenar 8 caracteres 
    -- PRA SABER LA HORA EXACTA SE MANEJA DATETIME
    fecha_nacimiento DATE, -- sera solamente fecha
    created_at DATETIME NOT NULL, -- sera fecha y hora, minuto, segundo
    sexo ENUM('MASCULINO','FEMENINO','OTRO','HELICOPTERO'), -- solamente podra tener los valores definidos
    estado BOOL -- Sera true o false
    
);
-- sirve ra modificar el nombre de una columna
-- ALTER TABLE personas RENAME COLUMN nombre TO nombrecito;

-- AHORA NGRESAMOS LOS DATOS
-- DML (data Mnipulacion Lunguage) Lenguje de Maniulacion de Datos
-- INSERT : ingresar nueva informcion a una tabla en especifico

INSERT INTO personas( nombre,dni, fecha_nacimiento, sexo, estado, created_at) VALUES 
					( 'Eliseo', '77137541','2000-12-12', 'MASCULINO', true, now());
INSERT INTO personas( nombre,dni, fecha_nacimiento, sexo, estado, created_at) VALUES 
					( 'Rogelio', '56789322','2000-12-12', 'MASCULINO', true, now());
INSERT INTO personas( nombre,dni, fecha_nacimiento, sexo, estado, created_at) VALUES 
					( 'Pedro', '48571455','2000-12-12', 'MASCULINO', true, now());
-- SELECT : leer los datos de una determinada tabla o

SELECT nombre, id FROM personas;

-- DTL (LENGUAJE DE DEFINICION DE DATOS) O (DATA DEFINITION LANGUAGE)
-- CREATE: Crear tablas, bases de datos y funciones y procedimientos almacenados entre otros

-- DROP: Sirve para ELIMINAR completamente toda una tabla, una base de datos, un estructura
 -- DROP TABLE personas ; 
SELECT nombre, id FROM personas;

SELECT * FROM personas  WHERE nombre = 'eliseo' AND estado = true;
SELECT * FROM personas WHERE nombre = 'eliseo' OR estado = false;

-- CREAR UNA TABLA LLAMADA ACTIVIDADES EN LA CUAL TENGAMOS EL ID, NOMBRE, INTENSIDAD Y SU 
-- ESTADO, EL ID TIENE QUE SER PK Y UNIQUE, EL NOMBRE NO PUEDE EXCEDER LOS 20 CARACTERES,
-- LA INTENSIDAD DEBE SER BAJA, MEDIA, ALTA O MUY ALTA Y SU ESTADO V O F
CREATE TABLE actividades(
	id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT ,
    nombre VARCHAR(20),
    intensidad ENUM('baja','media','alta','muy alta'),
    estado BOOL,
    persona_id INT ,
    -- para crear las relaciones
    FOREIGN KEY(persona_id) REFERENCES personas(id)
);
-- alter table actividades add persona_id int;
-- alter table actividades add foreign key(persona_id) references personas(id);
INSERT INTO actividades ( nombre, intensidad, estado, persona_id) VALUES 
						('PARRILLADAS','ALTA',TRUE,1);
                   
select * from actividades;
INSERT INTO actividades (nombre, intensidad, estado, persona_id) VALUES
                        ('MANEJAR','MEDIA',false, 2),					
                        ('COCINAR','ALTA', true, 1),
                        ('DISEÑAR','BAJA',false, 3) ;
                        

SELECT * FROM ACTIVIDADES;
SELECT * FROM personas;
INSERT INTO personas (nombre, dni, fecha_nacimiento, sexo, estado, created_at) VALUES
                     ('Patricio', '15934757', '1991-08-01', 'helicoptero', true, now());

INSERT INTO actividades (nombre, intensidad, estado) VALUES
                        ('NADAR', 'ALTA', true);
select * from personas inner join actividades ON personas.id = actividades.persona_id;
select * from personas left join actividades on personas.id = actividades.persona_id;

select * from personas right join actividades on personas.id = actividades.persona_id;

select * from personas left join actividades on personas.id = actividades.persona_id union 
select * from personas right join actividades on personas.id = actividades.persona_id;
drop table personas;

-- mostrar todas las personas cuya intencidad sea alta,
-- mostrar todos los registros cuyos sexos sea masculino o su estado de la actividad sea true
-- mostrar las personas que no tengan actividades
select * from personas inner join actividades where actividades.intensidad = 'ALTA';

select * from personas INNER JOIN ACTIVIDADES  WHERE actividades.ESTADO = TRUE OR   PERSONAS.SEXO = 'mASCULINO';

select * from personas   left JOIN  ACTIVIDADES on personas.id = actividades.persona_id
where ACTIVIDADES.persona_id is null;