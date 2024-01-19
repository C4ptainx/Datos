import requests
import os
from requests_oauthlib import OAuth1
import twitter

# Llaves y tokens obtenidos al crear una App en developers.twitter.com
consumer_key = "9IZoNJM5xg6LnjRZe83M6awXG" 
consumer_secret = "w16NWb9TB2Ns3prtU0KiTH390EDeYsur7a0wsxoxelhg3o11cJ"  

# Tokens de acceso de la cuenta de twitter
access_token = "1748141130070515712-M5S0267nlrj334Rrgbi4tvjdgTuwRe"  
access_token_secret= "HmxezDdYFc4KGC6KAQa9mhZ7CYpK7fg87k5xqehcn0sy9"  

api = twitter.Api(consumer_key=consumer_key, 
                  consumer_secret= consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret
                  )

# Búsqueda de Tweets sobre educación
query = 'educación' 
count = 10

search_results = api.GetSearch(term=query, count=count)

# Imprimir Tweets
print(f"Búsqueda de '{query}'")