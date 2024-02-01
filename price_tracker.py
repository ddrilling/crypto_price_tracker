import requests

url = 'https://api.coingecko.com/api/v3/simple/price'

def getPrice(ids: str):
    params = {
        'ids': ids,
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        jsonResponse = response.json()
        price = jsonResponse[ids]['usd']
        return price
    else:
        return 'Connection Error or Invalid ids'


"""
#for testing purposes
def main():
    ids = input('Enter the ids of the requested crypto asset: ')
    getPrice(ids)

if __name__ == '__main__':
    main()
"""