# from crawl import normalize_url
# from crawl import gethtml
# from parse_html import get_urls_html
from crawlers.path_crawl import crawlpage

def main():
    scr=crawlpage('https://wagslane.dev')
    print(scr)
    # htmlpa=gethtml('https://wagslane.dev')
    # print(get_urls_html(htmlpa,'https://wagslane.dev'))
if __name__ == "__main__":
    main()
