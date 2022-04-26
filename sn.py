from colorama import init, Fore
from mcstatus import JavaServer
from geoip import geolite2
from colorama import Style
from colorama import Back       #импортс
from ping3 import ping
from time import sleep
import requests
import json
import urllib.request
import os
import sys

def sn(server):
    servername = server.replace("s -n ", "")

    txt = 'https://api.mcsrvstat.us/2/server'
    aboba = txt.replace("server", servername)
    resp = requests.get(aboba)
    resp = json.loads(resp.text)
    good = resp['online']

    if good == True:
        server_stats = 1
    else:
        server_stats = 0

# тут тоже самое что и snpro но без всех доп функций

    print(Back.WHITE + '   ', end = '')
    print(Back.WHITE + Fore.BLACK + servername, end = '')
    print(
            Fore.BLACK + '                                                                                                                           ', end = '')

    if server_stats == 1:
        print(Fore.GREEN + '[ UP ]')

    else:
        print(Fore.RED + ' [DOWN]')

