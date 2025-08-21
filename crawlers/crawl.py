from urllib.parse import urlparse
import requests

from urllib.parse import urlparse, urlunparse

def normalize_url(url: str) -> str:
    parsed = urlparse(url)

    scheme = parsed.scheme.lower() or "http"
    netloc = parsed.netloc.lower()

    if netloc.startswith("www."):
        netloc = netloc[4:]

    path = parsed.path or "/"

    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")

    if path.endswith("index.html"):
        path = path[: -len("index.html")] or "/"

    return f"{scheme}://{netloc}{path}"


output=normalize_url('http://www.example.com')
print(output)
def get_html(url):
    try:
        response = requests.get(url)  #request from provided url 
    except Exception as e:
        raise Exception(f"network error while fetching {url}: {e}")

    if response.status_code > 399:
        raise Exception(f"got HTTP error: {response.status_code} {response.reason}")
    

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise Exception(f"got non-HTML response: {content_type}")
        #if it not the html content

    return response.text


def safe_get_html(url):
    try:
        return get_html(url)
    except Exception as e:
        print(f"{e}")
        return None