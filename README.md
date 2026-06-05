# 🏆 Estadísticas de Jugadores - Liga Profesional de Fútbol 2026

Proyecto de análisis de datos sobre los jugadores de la Liga Profesional de Fútbol Argentina 2026. Incluye procesamiento de datos con Python, almacenamiento en MySQL y visualización en Power BI.

## 🎯 Objetivo

Construir un pipeline de datos completo que permita analizar el rendimiento de los jugadores de la liga argentina, desde la extracción de datos en Excel hasta la visualización en un dashboard interactivo.

## 🛠️ Tecnologías utilizadas

- **Python** → procesamiento y carga de datos
- **Pandas** → lectura y transformación del archivo Excel
- **MySQL** → almacenamiento de los datos
- **Power BI** → visualización y dashboard (en desarrollo)

## 📁 Estructura del proyecto

```
liga-argentina-stats/
│
├── .env.example          → variables de entorno necesarias
├── .gitignore
├── README.md
│
├── data/
│   └── jugadores.xlsx    → dataset con 824 jugadores
│
├── powerbi/
│   └── liga_argentina_proyecto.pbix
│
├── sql/
│   ├── schema.sql
│   └── consultas.sql
│
└── src/
    └── cargar_datos.py
```

## 🗄️ Base de datos

El proyecto usa tres tablas relacionadas entre sí:

- **equipos** → los 30 equipos de la liga
- **jugadores** → 824 jugadores con sus datos personales
- **estadisticas** → goles, asistencias, minutos, amarillas y rojas por jugador

## 📊 Análisis disponibles

Las consultas están disponibles en `sql/consultas.sql`.

- Top 10 goleadores de la liga
- Top 10 jugadores con más asistencias
- Jugadores con más tarjetas amarillas
- Goles totales por equipo

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/FrancoMLS/liga-argentina-stats.git
cd liga-argentina-stats
```

### 2. Instalar dependencias
```bash
pip install pandas openpyxl mysql-connector-python python-dotenv
```

### 3. Configurar variables de entorno
Crear un archivo `.env` basado en `.env.example` y completar con tus credenciales de MySQL:
```
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=liga_argentina_2026
```

### 4. Crear la base de datos
Ejecutar el archivo `sql/schema.sql` en MySQL Workbench.

### 5. Cargar los datos
```bash
python src/cargar_datos.py
```

## 👤 Autor

Franco Lonello Serra - [GitHub](https://github.com/FrancoMLS)
