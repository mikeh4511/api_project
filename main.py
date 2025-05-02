import requests
import os
from dotenv import load_dotenv

load_dotenv("api.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ORG_NAME = 'blizzard'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

url = f'https://api.github.com/orgs/{ORG_NAME}/repos'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(f"{repo['name']} - {repo['html_url']}")
else:
    print(f"Error: {response.status_code} - {response.json().get('message')}")
