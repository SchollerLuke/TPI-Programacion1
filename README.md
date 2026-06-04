# TPI Programacion 1

# Sistema de Gestión y Análisis de Países

## Descripción del Proyecto

Este proyecto consiste en una aplicación desarrollada en Python que permite gestionar y analizar información de países a partir de un archivo CSV. El sistema ofrece funcionalidades de consulta, filtrado, ordenamiento y generación de estadísticas sobre los datos almacenados. Su objetivo es aplicar conceptos fundamentales de Programación 1, como listas, diccionarios, funciones, estructuras condicionales y repetitivas, así como técnicas de procesamiento de datos.

---

## Datos de la Universidad y la Cátedra

**Universidad:** Universidad Tecnológica Nacional 
**Carrera:** Tecnicatura Universitaria en Programación
**Materia:** Programación 1  
**Año:** 2026  
**Comisiones:** 13 y 21

---

## Integrantes

- Schulz, Lucas Eliezer (CM21)
- Simbeni, Nazarena Rocío (CM13)

---

## Profesores

**Docente Titular:** Cinthia Rigoni 

---

## Estructura del Proyecto

```text
TPI-Programacion1/
│
├── programa.py
├── datos_paises.csv
├── README.md
│
├── funciones/
│   ├── busqueda.py
│   ├── estadisticas.py
│   ├── ordenamiento.py
│   └── principales.py
│
└── docs/
    └── informe.pdf
```

### Descripción de los archivos

| Archivo | Descripción |
|----------|------------|
| `programa.py` | Programa principal |
| `datos_paises.csv` | Dataset con información de países |
| `README.md` | Documentación del proyecto |
| `funciones/busqueda.py` | Código con las funciones de búsqueda |
| `funciones/estadisticas.py` | Código con las funciones de estadísticas |
| `funciones/ordenamiento.py` | Código con las funciones de ordenamiento |
| `funciones/principales.py` | Código con las funciones principales |
| `docs/informe.pdf` | Informe del trabajo |

---

## Instrucciones de Ejecución

### Requisitos

- Python 3.10 o superior

### Ejecutar el programa

```bash
python programa.py
```

---

## Librerías Utilizadas

Este proyecto utiliza únicamente librerías estándar de Python:

- `csv`

No requiere instalación de dependencias externas.

---

## Repositorio y Video

### Repositorio GitHub

https://github.com/SchollerLuke/TPI-Programacion1

### Video Demostrativo

https://youtu.be/XXXXXXXXXXX

---

## Ejemplos de Entrada y Salida

### Menú Principal

**Entrada**

```text
1. Agregar país
2. Actualizar datos
3. Buscar país por nombre
4. Buscar país por filtro
5. Ordenar países por filtro
6. Mostrar estadísticas
7. Salir

Seleccione una opción: 2
```

**Salida**

```text
Ingrese el nombre del país: Argentina

País encontrado:
Nombre: Argentina
Población: 47067441
Superficie: 2780400 km²
Continente: América
```

---

### Estadísticas

**Salida**

```text
Cantidad total de países: 195

Continente con más países: África

País con mayor población:
India - 1428627663 habitantes

País con mayor superficie:
Rusia - 17098242 km²
```

---

## Dataset Utilizado

Cada país está representado mediante los siguientes atributos:

| Campo | Tipo |
|---------|---------|
| Nombre | String |
| Población | Integer |
| Superficie en km² | Integer |
| Continente | String |

---

## Objetivos del Proyecto

- Aplicar listas y diccionarios.
- Implementar funciones para modularizar el código.
- Trabajar con archivos CSV.
- Utilizar estructuras condicionales y repetitivas.
- Realizar búsquedas, filtrados y ordenamientos.
- Generar estadísticas e indicadores a partir de datos.
