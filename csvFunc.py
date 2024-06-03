import pandas as pd

def get_coordsCSV(city1):
    data = pd.read_csv("worldcities.csv")
    city = city1.city
    country = city1.country
    df = data[(data['city'] == city) & (data['country'] == country)]
    if df.empty:
        print(f"No se encontraron coordenadas para {city}, {country} en el archivo CSV.")
        return None, None
    else:
        lat = df.iloc[0]['lat']
        lng = df.iloc[0]['lng']
        return float(lat), float(lng)
