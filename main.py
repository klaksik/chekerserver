from colorama import init, Fore
from mcstatus import JavaServer
from geoip import geolite2
from colorama import Style
from colorama import Back       #импортс
from ping3 import ping
from time import sleep
from s import s
from sall import sall
from sn import sn
from snpro import snpro
import requests
import json
import urllib.request
import os
import sys

while True:
    init(autoreset=True)#без этого не работают цвета на винде

    print("list command  you gay((( uwu \nOptions:\n"
				    "\t(s) stats all servers\n"
                    "\t(s -all) viev all info\n"                  #это инфа 
				    "\t(s -n server) you server info\n"
                    "\texit\n"
				    "\t(s -n -all server) you server all info\n")


    servertest = input('->') # штука для красивого импута реально прикольно да?






    if 's -n -all' in servertest:
        snpro(servertest)

    elif 's -n' in servertest:
        sn(servertest)

    elif 's -all' in servertest:
        sall('play.vanilla-mc.xyz')
        sall('vanilla.makotomc.ru')
        sall('    seven-lights.ru')
        sall('           2b2t.org')
        sall('    12.pepeland.net')
    elif 's' in servertest:
        s('play.vanilla-mc.xyz')
        s('vanilla.makotomc.ru')
        s('    seven-lights.ru')
        s('           2b2t.org')
        s('    12.pepeland.net')
    elif 'exit' in servertest:
        sys.exit()













