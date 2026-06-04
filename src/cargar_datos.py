import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()
print("Conexión exitosa")

df = pd.read_excel("data/jugadores.xlsx", header=1)

df = df.rename(columns={
    "Player": "nombre",
    "Nation": "nacionalidad",
    "Pos": "posicion",
    "Squad": "equipo",
    "Age": "edad",
    "Born": "anio_nacimiento",
    "MP": "partidos_jugados",
    "Starts": "partidos_titular",
    "Min": "minutos",
    "Gls": "goles",
    "Ast": "asistencias",
    "CrdY": "amarillas",
    "CrdR": "rojas",
})

df["edad"] = df["edad"].str.split("-").str[0]

equipos = df["equipo"].dropna().unique()
equipo_ids = {}

for equipo in equipos:
    cursor.execute(
        "INSERT IGNORE INTO equipos (nombre) VALUES (%s)", (equipo,)
    )
    cursor.execute("SELECT id_equipo FROM equipos WHERE nombre = %s", (equipo,))
    equipo_ids[equipo] = cursor.fetchone()[0]

conn.commit()
print(f"Equipos insertados: {len(equipos)}")

for _, row in df.iterrows():
    nombre = row.get("nombre")
    if pd.isna(nombre):
        continue

    id_equipo = equipo_ids.get(row.get("equipo"))

    cursor.execute("""
        INSERT INTO jugadores (nombre, nacionalidad, posicion, id_equipo, edad, anio_nacimiento)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        str(nombre),
        str(row.get("nacionalidad", "")) or None,
        str(row.get("posicion", "")) or None,
        id_equipo,
        str(row.get("edad", "")) or None,
        int(row["anio_nacimiento"]) if pd.notna(row.get("anio_nacimiento")) else None,
    ))

    id_jugador = cursor.lastrowid

    cursor.execute("""
        INSERT INTO estadisticas
        (id_jugador, partidos_jugados, partidos_titular, minutos, goles, asistencias, amarillas, rojas, goles_x90, asistencias_x90)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        id_jugador,
        int(row.get("partidos_jugados", 0) or 0),
        int(row.get("partidos_titular", 0) or 0),
        int(float(str(row.get("minutos", 0)).replace(",", "") or 0)),
        int(row.get("goles", 0) or 0),
        int(row.get("asistencias", 0) or 0),
        int(row.get("amarillas", 0) or 0),
        int(row.get("rojas", 0) or 0),
        float(row.get("goles_x90", 0) or 0),
        float(row.get("asistencias_x90", 0) or 0),
    ))

conn.commit()
print("Jugadores y estadísticas insertados")