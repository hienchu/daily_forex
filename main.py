import requests
import json
import os
from datetime import date, timedelta

def get_forex_on_date(dt):
  ak = os.getenv('POLYGON_API_KEY')
  url = f"https://api.polygon.io/v2/aggs/grouped/locale/global/market/fx/{dt}?adjusted=true&apiKey={ak}"
  response = requests.get(url)
  print(response.status_code)
  rates = [(r['T'], r['c'], r['t']) for r in response.json()['results']]
  return rates

yesterday = date.today() - timedelta(days=1)
rates = get_forex_on_date(yesterday.strftime("%Y-%m-%d"))
json.dump(rates, open(f'rates_{yesterday}.json', 'w'))
