import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
    'start':'1',
    'limit':'5',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'Your_API_Key', # Replace 'Your_API_Key' with your actual API key
}

response = requests.get(url, headers=headers, params=parameters)
data = response.json()

if 'data' in data:
    for currency in data['data']:
        name = currency['name']
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']
        percent_change_24h = currency['quote']['USD']['percent_change_24h']
        price_change_24h = price * (percent_change_24h / 100)
        total_price = price + price_change_24h
        if name == "Bitcoin":
            if total_price < 40000:
                print(name + " (" + symbol + ") - " + "$" + str(round(total_price, 2)) + " (" + str(
                    round(percent_change_24h, 2)) + "%) - ALERT: Price is below $40,000!")
            else:
                print(name + " (" + symbol + ") - " + "$" + str(round(total_price, 2)) + " (" + str(
                    round(percent_change_24h, 2)) + "%)")
        elif name == "Ethereum":
            if total_price < 3000:
                print(name + " (" + symbol + ") - " + "$" + str(round(total_price, 2)) + " (" + str(
                    round(percent_change_24h, 2)) + "%) - ALERT: Price is below $3,000!")
            else:
                print(name + " (" + symbol + ") - " + "$" + str(round(total_price, 2)) + " (" + str(
                    round(percent_change_24h, 2)) + "%)")
        else:
            print(name + " (" + symbol + ") - " + "$" + str(round(total_price, 2)) + " (" + str(
                round(percent_change_24h, 2)) + "%)")
