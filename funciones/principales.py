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

def agregar_pais(paises, claves):
    """Función que permite agregar un país nuevo con todos sus datos
    
    Parámetros:
    ---
    * paises: lista de diccionarios con los datos de todos los países
    * claves: lista con las claves de los diccionarios
    """
    print("-"*40)
    
    while True:
        try:
            pais_nuevo = comprobar("Ingrese el nombre del país: ", False)
            if pais_nuevo == "": raise ValueError("No se permiten nombres vacíos")
            elif any(caracter.isdigit() for caracter in pais_nuevo): raise ValueError("No se permiten nombres numéricos")
            for linea in paises:
                if linea["Nombre"] == pais_nuevo: raise ValueError("El país ingresado ya existe")
        
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

    while True:
        try:
            continente = comprobar("Ingrese el continente del país: ", False)
            if continente == "": raise ValueError("No se permite población vacía")
            elif continente not in (
                "África",
                "América Central",
                "América Del Norte",
                "América Del Sur",
                "Asia",
                "Europa",
                "Oceanía"
            ): raise ValueError("Solo se pueden ingresar continentes existentes")

        except ValueError as e:
            print(f"Error: {e}")
        else: break

    paises.append({claves[0]: pais_nuevo, claves[1]: poblacion, claves[2]: superficie, claves[3]: continente})
    return paises

def actualizar_datos():
    pass

def buscar_nombre():
    pass

def buscar_filtro():
    pass

def ordenar_filtro():
    pass

def mostrar_estadisticas():
    pass