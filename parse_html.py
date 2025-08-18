from bs4 import BeautifulSoup

def get_urls_html(html_element:str,url:str):
    soup = BeautifulSoup(html_element, 'html.parser')
    found_links=[]
    for link in soup.find_all('a'): #to find all the <a> tags
        if url==link.get('href'):
            found_links.append(link.get('href'))
    return found_links
        
        


   