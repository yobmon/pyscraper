from urllib.parse import urlparse
import requests

def normalize_url(url:str):
    o=urlparse(url)
    
    parsedurl=str(o.hostname+o.path)

    return parsedurl
def gethtml(url:str):
    r = requests.get(url)
    if r.status_code>400:
        return 'bad requests'
    else:
        return r.text
        