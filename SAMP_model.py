#!/usr/bin/env python
# Usage: `python example.py (address=localhost) (port=7777) (rcon_password)`
# Example script demonstrating the use of this library
#
import sys
import configparser
from samp_client.client import SampClient
import json
import requests
from pathlib import Path

#==============================  VAR  ==========================================
BASE_DIR = Path(__file__).resolve().parent.parent

#===============================================================================
class SAMP:
    def __init__(self,*args):

        with SampClient(args[0],args[1],args[2]) as self.client:
            if not self.client.is_online():
                self.status = 'Server {}:{} is offline'.format(args[0],args[1])
                exit(1)
            self.info = self.client.get_server_info()

    def get_serv_players(self):
        return 'Игроки: {info.players}/{info.max_players}'.format(info=self.info)
    def get_serv_hostname(self):
        return 'Hostname: {info.hostname}'.format(info=self.info)
    def get_serv_gamemode_name(self):
        return 'Gamemode: {info.gamemode}'.format(info=self.info)
    def get_serv_lang(self):
        return 'Language: {info.language}'.format(info=self.info)
    def get_serv_pass(self):
        return  'Password: {info.password}'.format(info=self.info)




class JSONParser():
    def __init__(self, url):
        self.data = requests.get(url).json()

    def get_version(self):
        return str(self.data["verLauncher"])
    def get_download_link_launcher(self):
        return str(self.data['downLauncherLink'])
    def get_download_link_client(self):
        return str(self.data['downClientLink'])

class Configurator():
    def __init__(self,dir):
        self.path = dir

    def create_config(self,data):

        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "verLauncher", data["ver"])
        config.set("Settings", "lang", data["lang"])
        config.set("Settings", "pathClient", data["clientPath"])
        config.set("Settings", "checkSum", data["checksum"])
        config.set("Settings","onLoadOs",data["startup"])

        config.add_section("Web")
        config.set("Web", "UserName", data["UserName"])
        config.set("Web", "clientLink", data["clientLink"])
        config.set("Web","lastChoosedServer",data["lastServer"])
        config.set("Web","Servers",data["servers"])



        with open(self.path, "w") as config_file:
            config.write(config_file)

    def update_setting(section, setting, value):
        config = get_config(self.path)
        config.set(section, setting, value)

        with open(self.path, "w") as config_file:
            config.write(config_file)

    def get_setting(self, section, setting):

        config = get_config(slf.path)
        value = config.get(section, setting)
