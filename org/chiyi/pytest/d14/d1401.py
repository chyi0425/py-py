from time import time
from threading import Thread

import requests

# create a custom thread class by extends the Thread class

class DownloadHandler(Thread):

    def __init__(self,url):
         super().__init__()
         self.url = url
    
    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open('/Users/chiyi/'+filename,'wb') as f:
            f.write(resp.content)