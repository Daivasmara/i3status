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

with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD,XETHZUSD") as url:
    data = json.loads(url.read().decode())
    str = "₿ " + myround(data['result']['XXBTZUSD']['a'][0]) + "$ "
    str += "Ξ " + myround(data['result']['XETHZUSD']['a'][0]) + "$ "
    print(str, end='')

