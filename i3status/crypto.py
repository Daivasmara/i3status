#!/usr/bin/env python3
import json
import urllib.request

def myround (val, r=2):
  """
  Converts a string of float to rounded string
  @param {String} val, "42.551"
  @param {int} r, the decimal to round
  @return {string} "42.55" if r is 2
  """
  return "{:.{}f}".format(float(val), r)

with urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,lto-network,nimiq,fantom&vs_currencies=usd") as url:
    data = json.loads(url.read().decode())
    str = "₿ " + str(data["bitcoin"]["usd"]) + " "
    str += "⟠ " + "{:.3f}".format(data["ethereum"]["usd"]) + " "
    str += "⚶ " + "{:.3f}".format(data["lto-network"]["usd"]) + " "
    str += "⎔ " + "{:.3f}".format(data["nimiq"]["usd"]) + " "
    str += "❏ " + "{:.3f}".format(data["fantom"]["usd"]) + " "
    print(str, end='')

