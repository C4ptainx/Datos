import json
import requests
import csv

# Autenticación en la API de Twitter
bearer_token = "AAAAAAAAAAAAAAAAAAAAAC%2FwrwEAAAAAF3Czfh1MWt8vdfCEOUYgHaUiAPE%3DrsxRPHW7VBaYnM2jPqtMCAcMuuocTcQQEobv7Y20QxNVouMJrV"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# Parámetros de búsqueda para educación
params = {
    "query": "education", 
    "max_results": 100
}

# Realiza la solicitud a la API
response = requests.get("https://api.twitter.com/2/tweets/search/recent", 
                        headers=headers, params=params)


tweets = response.json()

data = []
print(tweets)
for tweet in data:
    print(tweet['id'])
      # Decodificar el texto del tweet 
    text = json.loads(tweet['text'])
    print(text)