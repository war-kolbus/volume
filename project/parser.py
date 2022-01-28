import requests
import json

def parse_real_volume(market, asset, token):
    if market == "kucoin":
        res = requests.get("https://api.kucoin.com/api/v1/market/stats?symbol="+token+"-"+asset)
        volume = float(res.json()["data"]["volValue"])
        spread = (float(res.json()["data"]["sell"]) - float(res.json()["data"]["buy"]))/float(res.json()["data"]["buy"])
        return float(res.json()["data"]["volValue"])
    elif market == "gate":
        res = requests.get("https://data.gateapi.io/api/1/ticker/" + token + "_" + asset)
        vol = "vol_"+asset.lower()
        return float(res.json()[vol])
    elif market == "mxc":
        res = requests.get("https://www.mexc.com/open/api/v2/market/ticker?symbol=" + token + "_" + asset)
        vol = res.json()["data"][0]["volume"]
        price = res.json()["data"][0]["last"]
        return float(vol)*float(price)
    elif market == "bitmart":
        res = requests.get("https://api-cloud.bitmart.com/spot/v1/ticker?symbol=" + token + "_" + asset)
        vol = res.json()["data"]["tickers"][0]["quote_volume_24h"]
        return float(vol)
    elif market == "probit":
        res = requests.get("https://api.probit.com/api/exchange/v1/ticker?market_ids=" + token + "-" + asset)
        return float(res.json()["data"][0]["quote_volume"])
    elif market == "bitrue":
        res = requests.get("https://www.bitrue.com//api/v1/ticker/24hr?symbol=" + token + asset)
        return float(res.json()[0]["volume"])
    elif market == "hitbtc":
        res = requests.get("https://api.hitbtc.com/api/3/public/ticker/" + token + asset)
        return float(res.json()["volume_quote"])
    elif market == "xt":
        res = requests.get("https://api.xt.com/data/api/v1/getTicker?market=" + token.lower() + "_" + asset.lower())
        return float(res.json()["moneyVol"])
