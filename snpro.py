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

def snpro(server): #ооо это какая то хрень ладно это вся информация о сервере который ты выбрал
    servername = server.replace("s -n -all", "")# тут удаляется тег

    txt = 'https://api.mcsrvstat.us/2/server'
    aboba = txt.replace("server", servername)#тут заменятся в переменной txt  server на названия сервера который выбрали

    resp = requests.get(aboba)
    resp = json.loads(resp.text)# тут узнается онлайн он или нет
    good = resp['online']

    if good == True:
        server_stats = 1 # тут узнается онлайн он или нет
    else:
        server_stats = 0


    try:
        gay = str(resp['players']['online'])# тут узнается сколько игроков на сервере
    except:
        gay = str(('0'))# если ошибка то ноль игроков, логично?


    skolko_geev = len(gay) #моя любимая чась и так тут узнается сколько символов в числе игроков

    skolko_geev_up = '         ' # и так эта часть кода если игроков 123 то текст [ OK ] сдвигается а это преддотвращает это
    print(Back.WHITE + '  ', end ='')
    print(Back.WHITE + Fore.BLACK + servername, end='')
    print(Fore.BLACK + '                                                                                ', 'players =',
          gay, end='')
    if skolko_geev == 1:
        print('           ', end='')
    if skolko_geev == 2:
        print('          ', end='')
    if skolko_geev == 3:
        print('         ', end='')
    if skolko_geev == 4:
        print('        ', end='')
    if skolko_geev == 5:
        print('       ', end='')


    if server_stats == 1:
        print(Fore.GREEN + ' [ UP ]')

    else:
        print(Fore.RED + ' [DOWN]')
