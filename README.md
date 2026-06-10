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
│   ├── estadisticas.py
│   ├── filtrado.py
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
| `funciones/estadisticas.py` | Código con las funciones de estadísticas |
| `funciones/filtrado.py` | Código con las funciones de filtrado |
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
========================================
             MENU PRINCIPAL             
========================================
1. Agregar país
2. Actualizar datos
3. Buscar país por nombre
4. Buscar país por filtro
5. Ordenar países por filtro
6. Mostrar estadísticas
7. Salir y guardar
========================================
Seleccione una opción: 3
```

**Salida**

```text
----------------------------------------
Ingrese el país a buscar: Argentina
País encontrado: Argentina
Población: 42669500
Superficie: 2780400
Continente: América Del Sur
----------------------------------------
Presione enter para continuar...
```

---

### Estadísticas

**Entrada**

```text
========================================
          MENU DE ESTADISTICA           
========================================
1. País con menor y mayor población
2. Promedio de población
3. Promedio de superficie
4. Cantidad de países por continente
5. Volver al menú principal
========================================
Seleccione una opción: 4
```

**Salida**

```text
----------------------------------------
Lista de países por continente: 
>> África: 46
>> América Central: 19
>> América Del Norte: 3
>> América Del Sur: 10
>> Asia: 39
>> Europa: 39
>> Oceanía: 13
----------------------------------------
Presione enter para continuar...
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
