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
BASE_DIR = Path(__file__).resolve().parent

#===============================================================================

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


class SAMP:
    def __init__(self,ip,port):
        try:
            with SampClient(ip,int(port)) as self.client:
                if not self.client.is_online():
                    self.status = 'Offline'
                else:
                    self.status = 'Online'
                    self.info = self.client.get_server_info()
        except:
            self.status = 'Offline'
    def get_info(self):
        return self.info
    def get_status(self):
        return self.status
    def get_serv_players(self):
        return 'Онлайн: {info.players}/{info.max_players}'.format(info=self.info)
    def get_serv_hostname(self):
        return '{info.hostname}'.format(info=self.info)
    def get_serv_gamemode_name(self):
        return 'Gamemode: {info.gamemode}'.format(info=self.info)
    def get_serv_lang(self):
        return 'Language: {info.language}'.format(info=self.info)
    def get_serv_pass(self):
        return  'Password: {info.password}'.format(info=self.info)



class JSONParser():
    def __init__(self, url, status):
        if status == 1:
            self.data = requests.get(url).json()
        else:
            self.data = url

    def get_version(self):
        return str(self.data["verLauncher"])
    def get_download_link_launcher(self):
        return str(self.data['downLauncherLink'])
    def get_download_link_client(self):
        return str(self.data['downClientLink'])
    def get_servers(self):  
        serv = self.data['servers']
        res = "".join([i+"," for i in serv])
        return res[:-1]

    def get_servers_last(self):
        return str(self.data['servers'][0])
    def get_web_links(self):
        return self.data['webLinks']

class Configurator():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configurator, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.path = BASE_DIR.joinpath("config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(self.path)


    def create_config(self,data):


        self.config.add_section("Settings")
        self.config.set("Settings", "verLauncher", data["ver"])
        self.config.set("Settings", "lang", data["lang"])
        self.config.set("Settings", "pathClient", data["clientPath"])
        self.config.set("Settings", "checkSum", data["checksum"])
        self.config.set("Settings","onLoadOs",data["startup"])

        self.config.add_section("Web")
        self.config.set("Web", "UserName", data["UserName"])
        self.config.set("Web", "clientLink", data["clientLink"])
        self.config.set("Web","lastChoosedServer",data["lastServer"])
        self.config.set("Web","Servers",data["servers"])



        with open(self.path, "w") as config_file:
            self.config.write(config_file)

    def set_val(self,section, setting, value):
        self.config.set(section, setting, value)

        with open(self.path, "w") as config_file:
            self.config.write(config_file)

    def get_val(self, section, setting):
        value = self.config.get(section, setting)
        return value
