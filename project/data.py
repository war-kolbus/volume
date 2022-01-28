pairs = [
    "UBX_USDT",
    "UBX_ETH",
    "ARV_USDT",
    "ARV_BTC",
    "KLO_USDT",
    "ETHO_USDT",
    "ETHO_BTC",
    "OVR_USDT",
    "WELD_USDT",
    "KUB_USDT"
]

markets = [
    "kucoin",
    "gate",
    "mxc",
    "bitmart",
    "probit",
    "bitrue",
    "hitbtc",
    "xt",

]

def generate_data_for_web():
    data_dict_for_web = {}
    for pair in pairs:
        data_dict_for_web[pair] = dict()
        for market in markets:
            data_dict_for_web[pair][market] = {
                "cond": "good",
                "volume": "Good"
            }
    return data_dict_for_web
