import tweepy

consumer_key = "9IZoNJM5xg6LnjRZe83M6awXG" 
consumer_secret = "w16NWb9TB2Ns3prtU0KiTH390EDeYsur7a0wsxoxelhg3o11cJ"  

# Tokens de acceso de la cuenta de twitter
access_token = "1748141130070515712-M5S0267nlrj334Rrgbi4tvjdgTuwRe"  
access_token_secret= "HmxezDdYFc4KGC6KAQa9mhZ7CYpK7fg87k5xqehcn0sy9"  

client = tweepy.Client(consumer_key= consumer_key, 
                       consumer_secret= consumer_secret,
                       access_token=access_token, 
                       access_token_secret=access_token_secret)

query = "educación"
tweets = client.search_recent_tweets(query=query, max_results=100)

data = []

print(data)