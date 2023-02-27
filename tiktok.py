import requests
import credentials

def get_trending_hashtags():
    url = "https://api.tiktok.com/discovery/v1/trending/hashtags/"
    headers = {"Authorization": f"Bearer {credentials.tiktok_access_token}"}
    params = {"count": 100, "language": "en"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)