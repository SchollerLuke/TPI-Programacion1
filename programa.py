import csv
import funciones.principales

todos_los_continentes = [
    "África",
    "América Central",
    "América Del Norte",
    "América Del Sur",
    "Asia",
    "Europa",
    "Oceanía"
]

def lectura_inicial():
    paises = []
    try:
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as dataset:
            lector = csv.DictReader(dataset)
            for fila in lector:
                paises.append(fila)

    except FileNotFoundError:
        print("\nError: el archivo no existe")
    except PermissionError:
        print("\nError: otro programa puede tener abierto el archivo")
    except IndexError:
        print("\nError: índice fuera de rango, pueden faltar datos en el archivo")
    except ValueError:
        print("\nError: valor inválido en el archivo")
    except Exception as e:
            print(f"\nError inesperado: {e}")

    else: return paises

def escribir_archivo(contenido, claves):
    try:
        with open("datos_paises.csv", "w", newline="", encoding="utf-8") as dataset:
            escritor = csv.DictWriter(dataset, fieldnames=claves)
            escritor.writeheader()
            escritor.writerows(contenido)

    except PermissionError:
        print("Error: otro programa puede tener abierto el archivo")
    except Exception as e:
            print(f"Error inesperado: {e}")

def imprimir_menu(menu):

    match menu:

        case "principal":
            opciones = (1,8)
            print("\n" + "=" * 40)
            print("MENU PRINCIPAL".center(40))
            print("=" * 40)
            print("1. Agregar país")
            print("2. Actualizar datos")
            print("3. Buscar país por nombre")
            print("4. Buscar país por filtro")
            print("5. Ordenar países por filtro")
            print("6. Mostrar estadísticas")
            print("7. Salir y guardar")
            print("=" * 40)

        case "buscar":
            opciones = (1,5)
            print("\n" + "=" * 40)
            print("MENU DE BUSQUEDA".center(40))
            print("=" * 40)
            print("1. Por continente")
            print("2. Rango de población")
            print("3. Rango de superficie")
            print("4. Volver al menú principal")
            print("=" * 40)

        case "ordenar":
            opciones = (1,5)
            print("\n" + "=" * 40)
            print("MENU DE ORDENAMIENTO".center(40))
            print("=" * 40)
            print("1. Por nombre")
            print("2. Por población")
            print("3. Por superficie")
            print("4. Volver al menú principal")
            print("=" * 40)

        case "estadistica":
            opciones = (1,6)
            print("\n" + "=" * 40)
            print("MENU DE ESTADISTICA".center(40))
            print("=" * 40)
            print("1. País con menor y mayor población")
            print("2. Promedio de población")
            print("3. Promedio de superficie")
            print("4. Cantidad de países por continente")
            print("5. Volver al menú principal")
            print("=" * 40)

    while True:
        opcion = funciones.principales.comprobar("Seleccione una opción: ")
        if opcion in range(opciones[0], opciones[1]): break
        else: print("Error: opción ingresada inválida")
    return opcion

def main():
    print("\nIniciando programa de gestión y análisis de países...")
    paises = lectura_inicial()
    if paises == None: print("Solucione el error detectado en el archivo y vuelva a ejecutar el programa")
    else: claves = list(paises[0].keys())
    
    while paises != None:
        match imprimir_menu("principal"):
    
            case 1:
                paises = funciones.principales.agregar_pais(paises, claves, todos_los_continentes)
    
            case 2:
                pass
    
            case 3:
                pass
    
            case 4:
                pass      
    
            case 5:
                pass
    
            case 6:
                pass
    
            case 7:
                escribir_archivo(paises, claves)
                break
        
        input("Presione enter para continuar...")

if __name__ == "__main__":
    main()