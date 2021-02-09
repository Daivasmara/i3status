#!/usr/bin/env python3
import json
import urllib.request

with urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,lto-network,nimiq,fantom,serum,injective-protocol&vs_currencies=usd") as url:
    data = json.loads(url.read().decode())
    str = "₿ " + "${:,.0f}".format(data["bitcoin"]["usd"]) + "  "
    str += "⟠  " + "${:,.0f}".format(data["ethereum"]["usd"]) + "  "
    str += "⚶ " + "${:,.3f}".format(data["lto-network"]["usd"]) + "  "
    str += "  " + "${:,.3f}".format(data["fantom"]["usd"]) + "  "
    str += " " + "${:,.3f}".format(data["serum"]["usd"]) + "  "
    str += " " + "${:,.3f}".format(data["injective-protocol"]["usd"])
    print(str, end='')
