from . import principales

def por_continente(paises, claves, lista_continentes):

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

    if tipo == "poblacion": tipo = 1
    elif tipo == "superficie": tipo = 2

    min = principales.comprobar("Ingrese valor mínimo de rango: ")
    max = principales.comprobar("Ingrese valor máximo de rango: ")

    print("-"*40)

    nombres = []
    valor = []
    for linea in paises:
        if min <= int(linea[claves[tipo]]) <= max:
            nombres.append(linea[claves[0]])
            valor.append(linea[claves[tipo]])

    if nombres == []:
        print("No se han encontrado países en ese rango")
    else: 
        print(f"Lista de países en el rango:")
        for pais in nombres:
           print(f">> {pais}: {valor[nombres.index(pais)]}")
    print("-"*40)