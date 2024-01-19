import json
import requests
import csv

api_url = "https://api.datos.gob.mx/v1/inai.solicitudes"

response = requests.get(api_url)

print(response)

"""
datos = response.json()
print(datos)
"""

if response.status_code == 200:
  datos = json.loads(response.content)
    
  with open('data_extraida.csv', 'w', newline='') as data_csv:
    writer = csv.writer(data_csv)
    writer.writerow(['_id', 'FOLIO', 'FECHASOLICITUD', 'DEPENDENCIA', 'ESTATUS', 'TIPOSOLICITUD', 'DESCRIPCION'])
      
    for elemento in datos["results"]:
        
      id = elemento.get("_id")
      folio = elemento.get("FOLIO")  
      fecha_solicitud = elemento.get("FECHASOLICITUD")
      dependencia = elemento.get("DEPENDENCIA")
      estatus = elemento.get("ESTATUS")
      tipo_solicitud = elemento.get("TIPOSOLICITUD")
      descripcion = elemento.get("DESCRIPCIONSOLICITUD")
       
      writer.writerow([id, folio, fecha_solicitud, dependencia, estatus, tipo_solicitud, descripcion])

      """
        print(f"Id: {id}")  
        print(f"Folio: {folio}")    
        print(f"Solicitud: {fecha_solicitud}")
        print(f"Dependencia: {dependencia}")
        print(f"Estatus: {estatus}")
        print(f"Tipo: {tipo_solicitud}")
        print(f"Descripcion: {descripcion}")
       """
else:
  print("Error en api")
  print(f"Error en API, código {response.status_code}")

print("Datos exportados")