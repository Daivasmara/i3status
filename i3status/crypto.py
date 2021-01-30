#!/usr/bin/env python3
import json
import urllib.request
import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

with urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,lto-network,nimiq,fantom&vs_currencies=usd") as url:
    data = json.loads(url.read().decode())
    str = "₿ " + locale.currency(data["bitcoin"]["usd"], grouping=True) + "  "
    str += "⟠  " + locale.currency(data["ethereum"]["usd"], grouping=True) + "  "
    str += "⚶ " + locale.currency(data["lto-network"]["usd"], grouping=True) + "  "
    str += "⎔ " + locale.currency(data["nimiq"]["usd"], grouping=True) + "  "
    str += "❏ " + locale.currency(data["fantom"]["usd"], grouping=True)
    print(str, end='')
