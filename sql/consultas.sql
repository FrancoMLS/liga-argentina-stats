USE liga_argentina_2026;

-- Top 10 goleadores
SELECT j.nombre, e.nombre AS equipo, SUM(s.goles) AS total_goles
FROM jugadores j
JOIN equipos e ON j.id_equipo = e.id_equipo
JOIN estadisticas s ON j.id_jugador = s.id_jugador
GROUP BY j.nombre, e.nombre
ORDER BY total_goles DESC
LIMIT 10;

-- Top 10 asistencias
SELECT j.nombre, e.nombre AS equipo, SUM(s.asistencias) AS total_asistencias
FROM jugadores j
JOIN equipos e ON j.id_equipo = e.id_equipo
JOIN estadisticas s ON j.id_jugador = s.id_jugador
GROUP BY j.nombre, e.nombre
ORDER BY total_asistencias DESC
LIMIT 10;

-- Jugadores con más amarillas
SELECT j.nombre, e.nombre AS equipo, s.amarillas
FROM jugadores j
JOIN equipos e ON j.id_equipo = e.id_equipo
JOIN estadisticas s ON j.id_jugador = s.id_jugador
ORDER BY s.amarillas DESC
LIMIT 10;

-- Goles totales por equipo
SELECT e.nombre AS equipo, SUM(s.goles) AS total_goles
FROM equipos e
JOIN jugadores j ON e.id_equipo = j.id_equipo
JOIN estadisticas s ON j.id_jugador = s.id_jugador
GROUP BY e.nombre
ORDER BY total_goles DESC;