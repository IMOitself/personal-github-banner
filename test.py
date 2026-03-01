import os
import requests

TOKEN = os.getenv("ACCESS_TOKEN")
URL = "https://api.github.com/graphql"

query = """
{
    viewer {
        login
    }
}
"""

headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.post(URL, json={'query': query}, headers=headers)

if(TOKEN is None):
    print("access token is None")
else:
    print(response.json())
