from . import busqueda
from . import ordenamiento
from . import estadisticas

def comprobar(texto, entero=True):
    """Función que comprueba validez de datos ingresados
    
    Parámetros:
    ---
    * texto: se ingresa un texto para indicarle al usuario que debe ingresar
    * entero: valor por defecto en True si se ingresa un entero
    (si se ingresa en False, indica que es un string)
    """

    while True:
        try:
            ingreso = input(texto).title()
            if entero == True: ingreso = int(ingreso)
            break

        except ValueError:
            print("Error: valor inválido")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
    return ingreso

def quitar_tildes(texto):
    """Función para quitar las tildes de una palabra o texto
    
    Parámetros:
    ---
    * texto: palabra o texto que se ingresa para quitarle la tilde
    """

    tupla_tilde = ("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    texto_final = []

    if any(letra in tupla_tilde[0] for letra in texto):

        for palabra in texto.split():
            palabra_final = ""
    
            for letra in palabra:
                if letra in tupla_tilde[0]: letra = tupla_tilde[1][tupla_tilde[0].index(letra)]
                palabra_final += letra
    
            texto_final.append(palabra_final)
        texto_final = " ".join(texto_final)

    else: texto_final = texto
    return texto_final

def cambiar_datos(paises, claves, opcion=str):
    """Función que permite cambiar datos de un país o agregarlos
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    * opcion: indica si se ingresa para agregar o para actualizar
    """
    print("-"*40)

    while True:
        try:
            pais = comprobar("Ingrese el nombre del país: ", False)
            if pais == "": raise ValueError("No se permiten nombres vacíos")
            elif any(caracter.isdigit() for caracter in pais): raise ValueError("No se permiten nombres numéricos")
            else :
                encontrado = False
                for linea in paises: 
                    if linea[claves[0]] == pais or quitar_tildes(linea[claves[0]]) == pais:
                        encontrado = True
                        break
                if opcion == "agregar" and encontrado: raise ValueError("El país ingresado ya existe")
                if opcion == "actualizar" and not encontrado: raise ValueError("El país ingresado no se encontró en la lista")
                     
        except ValueError as e:
            print(f"Error: {e}")
        else: break

    while True:
        try:
            poblacion = comprobar("Ingrese población del país: ")
            if poblacion == "": raise ValueError("No se permite población vacía")
            elif poblacion <= 0: raise ValueError("No se permite población negativa o nula")
        
        except ValueError as e:
            print(f"Error: {e}")
        else: break

    while True:
        try:
            superficie = comprobar("Ingrese superficie del país: ")
            if superficie == "": raise ValueError("No se permite superficie vacía")
            elif superficie <= 0: raise ValueError("No se permite superficie negativa o nula")
        
        except ValueError as e:
            print(f"Error: {e}")
        else: break

    return pais, poblacion, superficie

def agregar_pais(paises, claves, lista_continentes):
    """Función que permite agregar un país nuevo con todos sus datos
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    * lista_continentes: lista con todos los continentes
    """
    pais_nuevo, poblacion, superficie = cambiar_datos(paises, claves, "agregar")

    while True:
        try:
            continente = comprobar("Ingrese el continente del país: ", False)
            if continente == "": raise ValueError("No se permite población vacía")
            elif continente not in lista_continentes and all(continente != quitar_tildes(texto) for texto in lista_continentes): 
                raise ValueError("Solo se pueden ingresar continentes existentes")           

        except ValueError as e:
            print(f"Error: {e}")
        else: break

    for texto in lista_continentes:
        if continente == quitar_tildes(texto): 
            continente = texto
            break

    print("-"*40)

    paises.append({claves[0]: pais_nuevo, claves[1]: poblacion, claves[2]: superficie, claves[3]: continente})
    return paises

def actualizar_datos(paises, claves):
    """Función que permite actualizar los datos de un país
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    pais_actualizado, poblacion, superficie = cambiar_datos(paises, claves, "actualizar")

    print("-"*40)

    for i, linea in enumerate(paises):
        if linea[claves[0]] == pais_actualizado:
            paises[i].update({claves[1]: poblacion, claves[2]: superficie})

    return paises

def buscar_nombre(paises, claves):
    """Función que permite buscar un país por nombre (coincidencia parcial o exacta)
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    
    while True:
        try:
            pais_buscado = comprobar("Ingrese el país a buscar: ", False)
            if pais_buscado == "": raise ValueError("No se permiten nombres vacíos")
            elif any(caracter.isdigit() for caracter in pais_buscado): raise ValueError("No se permiten nombres numéricos")
            elif len(pais_buscado) < 3: raise ValueError("La búsqueda debe incluir por lo menos 3 carácteres")

        except ValueError as e:
            print(f"Error: {e}")
        else: break

    encontrados = []
    for i, linea in enumerate(paises):
        if pais_buscado in linea[claves[0]] or pais_buscado in quitar_tildes(linea[claves[0]]):
            encontrados.append(i)

    if len(encontrados) == 0: print("No se ha encontrado ningún país con esa búsqueda")
    elif len(encontrados) == 1:
        print(f"País encontrado: {paises[ encontrados[0] ][ claves[0] ]}")
        print(f"Población: {paises[ encontrados[0] ][ claves[1] ]}")
        print(f"Superficie: {paises[ encontrados[0] ][ claves[2] ]}")
        print(f"Continente: {paises[ encontrados[0] ][ claves[3] ]}")

    elif len(encontrados) > 1: 
        print("Países encontrados: ")
        for i in range(len(encontrados)):
            print(f">> {paises[ encontrados[i] ][ claves[0] ]}:")    
            print(f"- Población: {paises[ encontrados[0] ][ claves[1] ]}")
            print(f"- Superficie: {paises[ encontrados[0] ][ claves[2] ]}")
            print(f"- Continente: {paises[ encontrados[0] ][ claves[3] ]}")

    print("-"*40)    

def buscar_filtro():
    pass

def ordenar_filtro():
    pass

def mostrar_estadisticas():
    pass