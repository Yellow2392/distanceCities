import pandas as pd
import json

def get_coordsCSV(city1):
  data = pd.read_csv("worldcities.csv")
  city = city1.city
  country = city1.country
  df = data.query("city == @city and country == @country")
  df_json = str(df.to_json(orient='records', lines=True))
  result = json.loads(df_json)
  return result['lat'],result['lng']