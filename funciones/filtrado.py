from . import principales

def por_continente(paises, claves, lista_continentes):
    """Función que permite filtrar países por continente
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    * lista_continentes: lista con todos los continentes
    """
    continente = principales.ingrsar_continente(lista_continentes)
    print("-"*40)

    nombres = []
    for linea in paises:
        if linea[claves[3]] == continente:
            nombres.append(linea[claves[0]])

    print(f"Lista de países en {continente}")
    for pais in sorted(nombres):
       print(f">> {pais}")
    print("-"*40)

def rango(paises, claves, tipo):
    """Función que permite filtrar países por rango
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    * tipo: representa el tipo de filtro; población o superficie
    """
    if tipo == "poblacion": clave_filtro = 1
    elif tipo == "superficie": clave_filtro = 2

    min = principales.comprobar("Ingrese valor mínimo de rango: ")
    max = principales.comprobar("Ingrese valor máximo de rango: ")

    print("-"*40)

    nombres = []
    valor = []
    for linea in paises:
        if min <= int(linea[claves[clave_filtro]]) <= max:
            nombres.append(linea[claves[0]])
            valor.append(linea[claves[clave_filtro]])

    if nombres == []:
        print("No se han encontrado países en ese rango")
    else: 
        print(f"Lista de países en el rango:")
        for pais in nombres:
           print(f">> {pais}: {valor[nombres.index(pais)]}")
    print("-"*40)