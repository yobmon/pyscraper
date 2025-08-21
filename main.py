# from crawl import normalize_url
# from crawl import gethtml
# from parse_html import get_urls_html
from path_crawl import crawlpage

def main():
    crawlpage('https://wagslane.dev')
    # htmlpa=gethtml('https://wagslane.dev')
    # print(get_urls_html(htmlpa,'https://wagslane.dev'))
if __name__ == "__main__":
    main()
