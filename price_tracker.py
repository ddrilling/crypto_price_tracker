import requests

url = 'https://api.coingecko.com/api/v3'

def getPrice(ids: str):
    priceUrl = url + '/simple/price'
    params = {
        'ids': ids,
        'vs_currencies': 'usd'
    }
    response = requests.get(priceUrl, params=params)

    if response.status_code == 200:
        jsonResponse = response.json()
        price = jsonResponse[ids]['usd']
        roundedPrice = round(price, 4)
        return roundedPrice
    else:
        return 'Connection Error or Invalid ids'


def getTrending():
    trendingUrl = url + '/search/trending'
    response = requests.get(trendingUrl)

    trendingCoins = {}

    if response.status_code == 200:
        jsonResponse = response.json()
        for t in jsonResponse:
            for coins in t['coins']:
                for item in coins['item']:
                    name = item['name']
                    for data in item['data']:
                        price = data['price']
                        trendingCoins.update({name: price})

        return trendingCoins

    else:
        return 'Error occurred'


if __name__ == '__main__':
    x = getTrending()
    print(x)
"""
#for testing purposes
def main():
    ids = input('Enter the ids of the requested crypto asset: ')
    getPrice(ids)

if __name__ == '__main__':
    main()
"""