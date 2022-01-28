import json
from .parser import parse_real_volume
import threading


def toFixed(numObj):
    numObj = float(numObj)
    if numObj < 1000:
        return str(round(numObj, 2))
    elif numObj < 1000000:
        return str(round(numObj/1000, 2)) + "K"
    else:
        return str(round(numObj/1000000, 2)) + "M"


def generate_market_data_for_our_pairs(data_dict_for_web):

    with open('project/data/pairs.json') as json_file:
        all_our_pairs = json.load(json_file)
    threads = []
    for pair in all_our_pairs:
        thread = threading.Thread(target=thread_requesting, args=(all_our_pairs, pair, data_dict_for_web))
        threads.append(thread)
    for x in threads:
        x.start()
    for x in threads:
        x.join()
    return data_dict_for_web

def thread_requesting(all_our_pairs, pair, data_dict_for_web):
    token = pair.split("_")[0]
    asset = pair.split("_")[1]
    market = pair.split("_")[2]
    pred_volume = all_our_pairs[pair]["volume"]
    name = token + "_" + asset
    try:
        real_volume = parse_real_volume(market, asset, token)
        volume = toFixed(real_volume) + "/" + toFixed(pred_volume)
        if float(pred_volume) > float(real_volume):
            cond = "bad"
        else:
            cond = "good"
    except:
        cond = "warn"
        volume = "Ошибка:("
    board_market = {
        "cond": cond,
        "volume": volume,
    }
    data_dict_for_web[name][market] = board_market


