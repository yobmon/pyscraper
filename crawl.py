from urllib.parse import urlparse

def normalize_url(url:str):
    o=urlparse(url)
    
    parsedurl=str(o.hostname+o.path)

    return parsedurl
