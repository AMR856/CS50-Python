#!/usr/bin/python3
import requests
import sys
# print(f"${amount:,.4f}")
the_url =  'https://api.coindesk.com/v1/bpi/currentprice.json'
try:
    if len(sys.argv) == 2:
        bitcoin_count = float(sys.argv[1])
    response = requests.get(the_url)
    if response.status_code == 200:
        json_object = response.json()
        bitcoin_price = json_object['bpi']['USD']['rate']
        bitcoin_price_clean = float(bitcoin_price.replace(',', ''))
        final_price = bitcoin_price_clean * bitcoin_count
        print(f"${final_price:,.4f}")
    else:
        raise requests.RequestException
except (requests.RequestException, ValueError):
    sys.exit(1)
