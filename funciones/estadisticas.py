from . import principales

def mayor_menor_poblacion(paises, claves):
    """Función que muestra los datos de los países con la mayor y menor población
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    try:
        paises_ordenados = sorted(
        paises,
        key=lambda pais: int(pais[claves[1]]),
        reverse=True
        )
        # Ordena los países usando la población como criterio de comparación
    
    except ValueError:
        print("Error en el archivo: el dato de población no es entero")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        print("-"*40)
        print(f"País con mayor población: {paises_ordenados[0][claves[0]]} con {paises_ordenados[0][claves[1]]} habitantes")
        print(f"País con menor población: {paises_ordenados[-1][claves[0]]} con {paises_ordenados[-1][claves[1]]} habitantes")
    print("-"*40)

def promedio_poblacion(paises, claves):
    """Función que muestra el dato de promedio de población

    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    poblacion_total = 0

    try:
        for linea in paises:
            poblacion_total += int(linea[claves[1]])
    except ValueError:
        print("Error en el archivo: el dato de población no es entero")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else: print(f"Promedio de población en {len(paises)} paises: {(poblacion_total/len(paises)):.2f}")

    print("-"*40)

def promedio_superficie(paises, claves):
    """Función que muestra el dato de promedio de superficie

    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    superficie_total = 0

    try:
        for linea in paises:
            superficie_total += int(linea[claves[2]])
    except ValueError:
        print("Error en el archivo: el dato de población no es entero")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else: print(f"Promedio de superficie en {len(paises)} paises: {(superficie_total/len(paises)):.2f}")
    
    print("-"*40)

def cantidad_por_continente(paises, claves, lista_continentes):
    """Función que muestra el dato de cantidad de países por continente

    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    * lista_continentes: lista con todos los continentes
    """
    print("-"*40)
    paises_por_continente = dict.fromkeys(lista_continentes, 0)
    # Crea un diccionario con cada continente como clave e inicializa el contador en 0
    
    for linea in paises:
        continente = linea[claves[3]]
        paises_por_continente[continente] += 1

    print("Lista de países por continente: ")
    for continente in lista_continentes:
        print(f">> {continente}: {paises_por_continente[continente]}")
    print("-"*40)