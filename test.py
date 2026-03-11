import os
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("ACCESS_TOKEN")
if(TOKEN is None):
    print("access token is None")
    exit()


query = """
{
    viewer {
        login
    }
}
"""

headers = {"Authorization": f"Bearer {TOKEN}"}
URL = "https://api.github.com/graphql"
response = requests.post(URL, json={'query': query}, headers=headers)

print(response.json())
