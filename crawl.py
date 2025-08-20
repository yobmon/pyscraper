from urllib.parse import urlparse
import requests

def normalize_url(url:str):
    #used oly for checking if they are from one site
    #https://abcd.dev/path  ->abcd.dev/path
    o=urlparse(url)
    
    parsedurl=str(o.netloc+o.path)
    mini_parsedurl=parsedurl.lower()
    return mini_parsedurl.rstrip('/')

normalize_url('https://abcd.dev/path')
def gethtml(url:str):
    r = requests.get(url)
    if r.status_code>400:
        return 'bad requests'
    else:
        return r.text
        