from . import principales

def por_nombre(paises, claves):
    """Función que permite ordenar países por nombre
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    nombres = []
    for linea in paises:
        nombres.append(linea[claves[0]])
    
    print("Lista de paises ordenados por nombre")
    for pais in nombres:
        print(f">> {pais}")
    print("-"*40)


def ordenar(paises, claves, tipo):
    """Función que permite ordenar países según un filtro indicado
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    * tipo: representa el tipo de filtro; población o superficie
    """
    if tipo == "poblacion": clave_filtro = 1
    elif tipo == "superficie": clave_filtro = 2

    while True: 
        opcion = principales.comprobar("Seleccione una opción: (1) Descendente (2) Ascendente: ")
        if opcion in range(1,3): break
        else: print("Error: opción ingresada inválida")

    if opcion == 1: orden = "descendente"
    elif opcion == 2: orden = "ascendente"

    try:
        paises_ordenados = sorted(
        paises,
        key=lambda pais: int(pais[claves[clave_filtro]]),
        reverse=True if orden == "descendente" else False
        )   

    except ValueError:
        print("Error en el archivo: el dato de población o superficie no es entero")
        paises_ordenados = None
    except Exception as e:
        print(f"Error inesperado: {e}")
        paises_ordenados = None
    
    return paises_ordenados, orden

def por_poblacion(paises, claves):
    """Función que permite ordenar países por población
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    paises_ordenados, tipo = ordenar(paises, claves, "poblacion")

    if paises_ordenados == None: print("No se ha podido realizar el ordenamiento")
    else:
        print(f"Lista de paises ordenados por población de forma {tipo}")
        for pais in paises_ordenados:
            print(f">> {pais[claves[0]]}: {pais[claves[1]]}")
    print("-"*40)

def por_superficie(paises, claves):
    """Función que permite ordenar países por superficie
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    paises_ordenados, tipo = ordenar(paises, claves, "superficie")

    if paises_ordenados == None: print("No se ha podido realizar el ordenamiento")
    else:
        print(f"Lista de paises ordenados por superficie de forma {tipo}")
        for pais in paises_ordenados:
            print(f">> {pais[claves[0]]}: {pais[claves[2]]}")
    print("-"*40)