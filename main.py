
import requests


API_KEY = '346afe63965ce5cd36b787e95a304ae2'
CALLBACK_URL = 'https://0e437bbc.ngrok.io/callback'
API_ROOT = 'http://www.last.fm/api/auth/?api_key={}&cb={}'.format(API_KEY, CALLBACK_URL)


def main():
    response = requests.get(API_ROOT)
    data = response.json()
    print(data)


if __name__ == '__main__':
    main()
