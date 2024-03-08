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
        return 'Connection Error or Invalid id'


def getTrending():
    trendingUrl = url + '/search/trending'
    response = requests.get(trendingUrl)

    trendingCoins = {}
    if response.status_code == 200:
        jsonResponse = response.json()
        coins = jsonResponse['coins']
        for coin in coins[:10]:
            name = coin['item']['name']
            price = coin['item']['data']['price']
            image = coin['item']['small']
            trendingCoins[name] = {'price': price, 'image': image}
        return trendingCoins

    else:
        return 'Error occurred'
        


'''
#for testing purposes

if __name__ == '__main__':
    x = []
    x = getTrending()
    print(x)
'''