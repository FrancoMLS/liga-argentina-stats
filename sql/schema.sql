DROP DATABASE IF EXISTS liga_argentina_2026;
CREATE DATABASE liga_argentina_2026;
USE liga_argentina_2026;

CREATE TABLE equipos (
    id_equipo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE jugadores (
    id_jugador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    nacionalidad VARCHAR(20),
    posicion VARCHAR(10),
    id_equipo INT,
    edad VARCHAR(3),
    anio_nacimiento INT,
    FOREIGN KEY (id_equipo) REFERENCES equipos(id_equipo)
);

CREATE TABLE estadisticas (
    id_estadistica INT AUTO_INCREMENT PRIMARY KEY,
    id_jugador INT,
    partidos_jugados INT,
    partidos_titular INT,
    minutos INT,
    goles INT,
    asistencias INT,
    amarillas INT,
    rojas INT,
    goles_x90 DECIMAL(5,2),
    asistencias_x90 DECIMAL(5,2),
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);