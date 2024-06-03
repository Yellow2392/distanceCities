from haversine import haversine
from csvFunc import get_coordsCSV
from apiFunc import get_coordsAPI
from classes import City,Coords

ciudad1 = City()
ciudad1.city = "Tokyo"
ciudad1.country = "Japan"

ciudad2 = City()
ciudad2.city = "Lima"
ciudad2.country = "Peru"

coords1 = Coords()
coords2 = Coords()

coords1.lat, coords1.lng = get_coordsCSV(ciudad1)
coords2.lat, coords2.lng = get_coordsCSV(ciudad2)

print(haversine(coords1.lng,coords1.lat,coords2.lng,coords2.lat))

coords1.lat, coords1.lng = get_coordsAPI(ciudad1)
coords2.lat, coords2.lng = get_coordsAPI(ciudad2)

print(haversine(coords1.lng,coords1.lat,coords2.lng,coords2.lat))