from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_urls_html(html_element:str,url:str):
    soup = BeautifulSoup(html_element, 'html.parser')
    found_links=[]
    
    for link in soup.find_all('a'): #to find all the <a> tags
        if link.get('href'):
            absoluteurl=urljoin(url,link.get('href'))
            found_links.append(absoluteurl)
    #returns relative path from given the html provided using url a a basis        
    return found_links
        
        


   