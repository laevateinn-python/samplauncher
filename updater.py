from SAMP_model import Configurator,JSONParser
import requests
from pathlib import Path
import os
import sys
import rarfile
import zipfile
import click

TEMP_DIR = Path(os.environ["TEMP"]).resolve()

class updateLauncher:
    def __init__(self):
        self.cfg = Configurator()
        self.json = JSONParser("http://127.0.0.1:5000/api",1)

    def download(self,filepath):
        self.deleteOld(filepath)
        req = requests.get(self.json.get_download_link_launcher())
        open('filepath', 'wb').write(req.content)
    
    def deleteOld(self,filepath):
        os.remove(filepath)

class updateClient:
    def __init__(self):
        self.cfg = Configurator()
        self.json = JSONParser("http://127.0.0.1:5000/api",1)

    def download(self):
        self.file_name = TEMP_DIR.joinpath("client.zip")
        with open(self.file_name, "wb") as f:
            response = requests.get(self.json.get_download_link_client(), stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
    def install(self,path):
        z = zipfile.ZipFile(self.file_name,'r')
        z.extractall(path=path)
        


@click.command()
@click.argument('path')
@click.option('--ident', '-i')
def main(path,ident):
    if ident == "Launcher":
        c = updateLauncher()
        c.download(path)
    elif ident == "Client":
        c = updateClient()
        c.download()
        c.install(path)

if __name__ == "__main__":
    main()
