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

def sall(ip):
    txt = 'https://api.mcsrvstat.us/2/server'
    aboba = txt.replace("server", ip)




# это тоже саоме что и s но выдает доп инфу
    resp = requests.get(aboba)
    resp = json.loads(resp.text)
    good = resp['online']


    if good == True:
        server_stats = 1
    else:
        server_stats = 0

    try:
        gay = str(resp['players']['online'])
    except:
        gay = str(('0'))
    skolko_geev = len(gay)
    print(Back.WHITE + Fore.BLACK + '   ', end = '')
    print(Back.WHITE + Fore.BLACK + ip, end = '')
    skolko_geev_up = '         '
    print(Fore.BLACK + '                                                                                                    ', 'players =', gay, end='')
    if skolko_geev == 1:
        print('           ', end = '')
    if skolko_geev == 2:
        print('          ', end = '')
    if skolko_geev == 3:
        print('         ', end = '')
    if skolko_geev == 4:
        print('        ', end = '')
    if skolko_geev == 5:
        print('       ', end = '')

    if server_stats == 1:
        print(Fore.BLUE + '[ UP ]')

    else:
        print(Fore.RED + '[DOWN]')
