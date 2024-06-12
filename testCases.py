from haversine import haversine
from csvFunc import get_coordsCSV
from apiFunc import get_coordsAPI 
from classes import City, Coords

def calculate_distance_and_errors(coords1_csv, coords1_api, coords2_csv, coords2_api, actual_distance):
  distance_csv = haversine(coords1_csv[0], coords1_csv[1], coords2_csv[0], coords2_csv[1])
  distance_api = haversine(coords1_api[0], coords1_api[1], coords2_api[0], coords2_api[1])
  error_absolute_csv = abs(actual_distance - distance_csv)
  error_absolute_api = abs(actual_distance - distance_api)
  error_relative_csv = error_absolute_csv / actual_distance
  error_relative_api = error_absolute_api / actual_distance
  return distance_csv, distance_api, error_absolute_csv, error_absolute_api, error_relative_csv, error_relative_api

def test1():
  print("Test 1")
  param_Tokyo = City()
  param_Tokyo.city = 'Tokyo'
  param_Tokyo.country = 'Japan'
  param_Lima = City()
  param_Lima.city = 'Lima'
  param_Lima.country = 'Peru'

  # Coordenadas reales
  jp_coords = (35.6684103, 139.5760562)
  pe_coords = (-12.0257733, -77.3174469)

  # Distancia real
  actual_distance = 15490.18

  # Obtener coordenadas
  coords_jp_csv = get_coordsCSV(param_Tokyo)
  coords_jp_api = get_coordsAPI(param_Tokyo)
  coords_pe_csv = get_coordsCSV(param_Lima)
  coords_pe_api = get_coordsAPI(param_Lima)

  # Calcular distancias y errores
  distance_csv, distance_api, error_absolute_csv, error_absolute_api, error_relative_csv, error_relative_api = calculate_distance_and_errors(
      coords_jp_csv, coords_jp_api, coords_pe_csv, coords_pe_api, actual_distance
  )

  # Imprimir resultados
  print("Coordenadas reales de Tokyo, Japon: ", jp_coords)
  print("Coordenadas por csv de Tokyo, Japon: ", coords_jp_csv)
  print("Coordenadas por api de Tokyo, Japon: ", coords_jp_api)
  print("-----")
  print("Coordenadas reales de Lima, Peru: ", pe_coords)
  print("Coordenadas por csv de Lima, Peru: ", coords_pe_csv)
  print("Coordenadas por api de Lima, Peru: ", coords_pe_api)
  print("-----")
  print("Distancia real entre Tokyo y Lima: ", actual_distance)
  print("Distancia por csv entre Tokyo y Lima: ", distance_csv)
  print("Distancia por api entre Tokyo y Lima: ", distance_api)
  print("-----")
  print("Error absoluto (CSV): ", error_absolute_csv)
  print("Error absoluto (API): ", error_absolute_api)
  print("Error relativo (CSV): ", error_relative_csv)
  print("Error relativo (API): ", error_relative_api)
  print("-----")

def test2():
    print("Test 2")
    param_Paris = City()
    param_Paris.city = 'Paris'
    param_Paris.country = 'France'
    param_Lisbon = City()
    param_Lisbon.city = 'Lisbon'
    param_Lisbon.country = 'Portugal'

    # Coordenadas reales
    fr_coords = (48.856614, 2.3522219)
    pt_coords = (38.7222524, -9.1393366)

    # Distancia real
    actual_distance = 1452.31

    # Obtener coordenadas
    coords_fr_csv = get_coordsCSV(param_Paris)
    coords_fr_api = get_coordsAPI(param_Paris)
    coords_pt_csv = get_coordsCSV(param_Lisbon)
    coords_pt_api = get_coordsAPI(param_Lisbon)

    # Calcular distancias y errores
    distance_csv, distance_api, error_absolute_csv, error_absolute_api, error_relative_csv, error_relative_api = calculate_distance_and_errors(
        coords_fr_csv, coords_fr_api, coords_pt_csv, coords_pt_api, actual_distance
    )

    # Imprimir resultados
    print("Coordenadas reales de Paris, Francia: ", fr_coords)
    print("Coordenadas por csv de Paris, Francia: ", coords_fr_csv)
    print("Coordenadas por api de Paris, Francia: ", coords_fr_api)
    print("-----")
    print("Coordenadas reales de Lisbon, Portugal: ", pt_coords)
    print("Coordenadas por csv de Lisbon, Portugal: ", coords_pt_csv)
    print("Coordenadas por api de Lisbon, Portugal: ", coords_pt_api)
    print("-----")
    print("Distancia real entre Paris y Lisbon: ", actual_distance)
    print("Distancia por csv entre Paris y Lisbon: ", distance_csv)
    print("Distancia por api entre Paris y Lisbon: ", distance_api)
    print("-----")
    print("Error absoluto (CSV): ", error_absolute_csv)
    print("Error absoluto (API): ", error_absolute_api)
    print("Error relativo (CSV): ", error_relative_csv)
    print("Error relativo (API): ", error_relative_api)
    print("-----")