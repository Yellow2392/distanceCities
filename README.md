# Ingeniería de Software: Actividad
## Integrantes:
- Sebastian Tenorio
- Yoselyn Miranda

## Descripción de la aplicación
Este es un pequeño programa que permite medir las distancias entre 2 ciudades mediante 2 métodos que el usuario elija. Sea mediante el dataset `worldcities.csv` o mediante la api proporcionada por https://nominatim.openstreetmap.org

## Equipo con quienes colaboramos en su github:
https://github.com/CeciliaNatali/Tarea_Soft_Duplas

## Pruebas unitarias
Se implementaron 2 pruebas unitarias dentro del módulo `testCases.py` para corroborar la precisión de los datos y resultados obtenidos en ambos casos comparando con valores investigados de manera aparte.
En ese sentido como pruebas manuales tenemos:
| Test Case                           | Precondition                         | Test Steps                                                        | Test Data                      | Expected Result                                         |
|-------------------------------------|--------------------------------------|-------------------------------------------------------------------|-------------------------------|---------------------------------------------------------|
| Verificar distancia Lima - Tokyo | Usuario debe abrir el menú del programa | Elegir la opción 3 o 4 para calcular la distancia; Ingresar un nombre y un país válidos para la primera ciudad y segunda ciudad; y Dar a Enter para calcular | ("Lima","Peru"), ("Tokyo","Japan") |   Aproximadamente 15490.18 km  |
| Verificar distancia Paris - Lisbon | Usuario debe abrir el menú del programa | Elegir la opción 3 o 4 para calcular la distancia; Ingresar un nombre y un país válidos para la primera ciudad y segunda ciudad; y Dar a Enter para calcular | ("Paris","France"), ("Lisbon","Portugal") |   Aproximadamente 1452.31 km  |

### Resultados de casos de prueba
Los siguientes casos de prueba se corrieron mediante el menú ya implementado. Opcionalmente se puede optar por importar el módulo testCases anteriormente descrito y correrlo en lugar del menu dentro de `main.py`
#### Menu
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/2996b4e9-cf0b-4e2f-b603-bfe0a358d249)

#### Lima, Peru - Tokyo, Japan
##### Mediante CSV
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/3dc0c146-b09d-40e5-8646-0062d6b8fb53)

##### Mediante API
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/fbcf823a-8930-480a-b0dc-fd6b251779be)

#### Paris, France - Lisbon, Portugal
##### Mediante CSV
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/a673b58b-c61f-4f6e-813c-46255d0d02e6)

##### Mediante API
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/fb5a795b-3099-4ae4-bca1-692e0dcaba69)

## Casos extremos
Evaluamos adicionalmente dos casos particulares dentro del programa
#### Distancia entre una misma ciudad
##### Mediante CSV
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/0475b2ff-43cd-4f68-b839-8f81637421f3)

##### Mediante API
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/1a51c035-b823-4351-92aa-32401ddaffec)

#### Ciudad no existente
##### Mediante CSV
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/f6aca130-e928-4ace-a680-8272205b0ddb)

##### Mediante API
![image](https://github.com/Yellow2392/distanceCities/assets/103154944/4c0ed1fb-7e3e-45a0-81ce-6e12f9cb9c92)

## Notas
- La medición de la distancia entre dos ciudades funciona correctamente y entrega resultados bastante cercanos a lo que se espera.
- El caso particular de que se mida la distancia entre una misma ciudad funciona debido a que trivialmente la distancia entre un punto y sí mismo es 0.
- El caso de ciudad no existente se maneja apropiadamente en el método por csv al mostrar los debidos mensajes de error.
- Sin embargo, el caso de ciudad no existente no se maneja como se debe en el método por api. Esto se explica ya que la api retorna los resultados que más coincidan a la query enviada, siendo así que su retorno no será vacío. Para tal caso, se recomienda añadir algún mensaje que notifique al usuario la coincidencia más cercana para realizar el cálculo.
