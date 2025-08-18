from crawl import normalize_url
from crawl import gethtml
from parse_html import get_urls_html
def main():
    normalize_url('https://wagslane.dev')
    htmlpa=gethtml('https://wagslane.dev')
    get_urls_html(htmlpa)
if __name__ == "__main__":
    main()
