import requests

BITLY_API_URL = "https://api-ssl.bitly.com/v4/shorten"
ACCESS_TOKEN = "05044e0edb640f7093b74b3dcb730382d6a20a2d"  # Replace with your Bitly access token

def shorten_url(long_url):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "long_url": long_url,
        "domain": "bit.ly"
    }

    response = requests.post(BITLY_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        short_url = response.json().get("link")
        return short_url
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    
    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        print("Failed to shorten the URL.")
