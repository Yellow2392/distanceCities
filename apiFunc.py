import requests
import json

def get_coordsAPI(city1):
  api = f'https://nominatim.openstreetmap.org/search?q={city1.city},{city1.country}&format=json'
  headers = {'User-Agent': 'distanceCities/1.0 (jorge.tenorio@utec.edu.pe)'}
  response = requests.get(api, headers=headers)
  #print(f"Generated URL: {api}") 
  try:
      result = json.loads(response.text)
      if result:
          return float(result[0]['lat']), float(result[0]['lon'])
      else:
          raise ValueError("Empty result")
  except json.JSONDecodeError as e:
      print("Error decoding JSON:", e)
      print("Response text:", response.text)
      return 0.0, 0.0