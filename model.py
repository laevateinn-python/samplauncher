#!/usr/bin/env python
# Usage: `python example.py (address=localhost) (port=7777) (rcon_password)`
# Example script demonstrating the use of this library
#
import sys

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
                print('Server {}:{} is offline'.format(args[0],args[1]))
                exit(1)
            self.info = self.client.get_server_info()

    def get_serv_players(self):
        return 'Players: {info.players}/{info.max_players}'.format(info=self.info)
    def get_serv_hostname(self):
        return 'Hostname: {info.hostname}'.format(info=self.info)
    def get_serv_gamemode_name(self):
        return 'Gamemode: {info.gamemode}'.format(info=self.info)
    def get_serv_lang(self):
        return 'Language: {info.language}'.format(info=self.info)
    def get_serv_pass(self):
        return  'Password: {info.password}'.format(info=self.info)

    def rules(self):
        print("Server Rules:")
        for rule in self.client.get_server_rules():
            print("{rule.name}: {rule.value}".format(
                rule=rule,))


    def rcon(self):
        if self.client.rcon_password is None:
            self.client.rcon_password = input('RCON password:')
        print('Enter rcon commands or leave blank to exit. Example: cmdlist')
        while True:
            command = input('RCON: ')
            if not command:
                return
            for line in self.client.send_rcon_command(command):
                print(line)


class JSONParser():
    def __init__(self, url):
        self.data = json.load(requests.get(url).text)

    def get_version(self):
        return self.data["verLauncher"]
    def get_number_of_servers(self):
        return self.data["numServ"]
    def get_serv_array(self):
        return self.data["servers"]
    def get_download_link(self):
        return self.data['downloadLink']

class Configurator():
    def __init__(self,dir=BASE_DIR):
        self.cfg = dir.joinpath("config.ini")
        print(self.cfg)

    def get_metadata(self):
        n = []
        with open(self.cfg,'r') as f:
            for i in f:
                n.append(i.split('='))
        return n
    def generateConfig(self,f):
        with open(self.cfg,'w') as f:
            f.write(txt)
