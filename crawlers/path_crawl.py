from crawlers.crawl import safe_get_html   #get html foreach link
from html_parsing.parse_html import get_urls_html #return an array of links that found within page
from urllib.parse import urlparse
from crawlers.crawl import normalize_url
from html_parsing.extract_page import extract_page_data
def crawlpage(baseurl:str,current_url=None,pages=None):
    if current_url==None:
        current_url=baseurl
    if pages == None:
        pages={}  
    #the above is for first condition
    
    base_url_obj = urlparse(baseurl)
    current_url_obj = urlparse(current_url)

    if current_url_obj.netloc != base_url_obj.netloc:
        return pages
    #the above if the path is not in context of our link
    normalized_url = normalize_url(current_url)

    if normalized_url in pages:
          
        return pages  #prevent scraping one link more than once
   
    print(f"we currently scraping {current_url}")
    htmlelement=safe_get_html(current_url)
    
    if htmlelement is None:
        return pages
    
    pages[normalized_url]=extract_page_data(htmlelement,current_url)
    nex_links=get_urls_html(htmlelement,baseurl)
    
    for link in nex_links:
        pages=crawlpage(baseurl,link,pages)
    return pages  # the pages thats scraped


       





