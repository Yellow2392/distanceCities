import os
from haversine import haversine
from csvFunc import get_coordsCSV
from apiFunc import get_coordsAPI
from classes import City, Coords

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print("=== Menú Principal ===")
    print("1. Obtener coordenadas desde CSV")
    print("2. Obtener coordenadas desde API")
    print("3. Calcular distancia con CSV")
    print("4. Calcular distancia con API")
    print("5. Salir")

def obtener_ciudad():
    ciudad = City()
    ciudad.city = input("Ingresa el nombre de la ciudad: ")
    ciudad.country = input("Ingresa el nombre del país: ")
    return ciudad

def obtener_coordenadas_csv(ciudad):
    coords = Coords()
    coords.lat, coords.lng = get_coordsCSV(ciudad)
    if coords.lat is None or coords.lng is None:
        raise ValueError(f"No se pudieron obtener las coordenadas para {ciudad.city}, {ciudad.country} desde CSV.")
    return coords

def obtener_coordenadas_api(ciudad):
    coords = Coords()
    coords.lat, coords.lng = get_coordsAPI(ciudad)
    if coords.lat is None or coords.lng is None:
        raise ValueError(f"No se pudieron obtener las coordenadas para {ciudad.city}, {ciudad.country} desde API.")
    return coords

def calcular_distancia_csv(ciudad1, ciudad2):
    try:
        coords1 = obtener_coordenadas_csv(ciudad1)
        coords2 = obtener_coordenadas_csv(ciudad2)
        distancia = haversine(coords1.lng, coords1.lat, coords2.lng, coords2.lat)
        print(f"Distancia entre {ciudad1.city} y {ciudad2.city} (CSV): {distancia} km")
    except ValueError as e:
        print(e)

def calcular_distancia_api(ciudad1, ciudad2):
    try:
        coords1 = obtener_coordenadas_api(ciudad1)
        coords2 = obtener_coordenadas_api(ciudad2)
        distancia = haversine(coords1.lng, coords1.lat, coords2.lng, coords2.lat)
        print(f"Distancia entre {ciudad1.city} y {ciudad2.city} (API): {distancia} km")
    except ValueError as e:
        print(e)

def volver():
    input("\nPresiona Enter para volver al menú principal...")
    limpiar_pantalla()

def salir():
    print("Saliendo...")
    exit()

def menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            ciudad = obtener_ciudad()
            coords = obtener_coordenadas_csv(ciudad)
            print(f"Coordenadas de {ciudad.city} (CSV): ({coords.lat}, {coords.lng})")
            volver()
        elif opcion == '2':
            limpiar_pantalla()
            ciudad = obtener_ciudad()
            coords = obtener_coordenadas_api(ciudad)
            print(f"Coordenadas de {ciudad.city} (API): ({coords.lat}, {coords.lng})")
            volver()
        elif opcion == '3':
            limpiar_pantalla()
            print("Introduce los datos para la primera ciudad:")
            ciudad1 = obtener_ciudad()
            print("Introduce los datos para la segunda ciudad:")
            ciudad2 = obtener_ciudad()
            calcular_distancia_csv(ciudad1, ciudad2)
            volver()
        elif opcion == '4':
            limpiar_pantalla()
            print("Introduce los datos para la primera ciudad:")
            ciudad1 = obtener_ciudad()
            print("Introduce los datos para la segunda ciudad:")
            ciudad2 = obtener_ciudad()
            calcular_distancia_api(ciudad1, ciudad2)
            volver()
        elif opcion == '5':
            salir()
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    menu()
