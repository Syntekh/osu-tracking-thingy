import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def receiveToken(client_id, client_secret):
    token_url = "https://osu.ppy.sh/oauth/token"
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "public"
    }
    
    response = requests.post(token_url, data=data)

    token = response.json()["access_token"]
    return token

def stats(token, user):
    user_url = f"https://osu.ppy.sh/api/v2/users/{user}/osu"
    
    headers = {
        "Authorization": "Bearer " + token
        }
    
    response = requests.get(user_url, headers=headers)
    return response.json()

search_user = input("Enter a username: ")


try:
    data = stats(receiveToken(client_id, client_secret), search_user)

    country = data["country"]["name"]
    rank = data["statistics"]["global_rank"]
    pp = data["statistics"]["pp"]

    print(f"User: {search_user} \nCountry: {country} \nRank: #{rank} \nPerformance Points: {pp} PP")

except:
    print("This user doesn't seem to exist...")