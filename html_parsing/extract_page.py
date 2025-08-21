from bs4 import BeautifulSoup
def get_html_h1(html):
    soup=BeautifulSoup(html,'html.parser')
    h1_tag=soup.find('h1')
    #return the first h1 element from the link
    return  h1_tag.get_text(strip=True) if h1_tag else ""
def get_html_p(html):
    soup=BeautifulSoup(html,'html.parser')
    main_section=soup.find('main')  #first find within main section 
    if main_section:
        p_tag=main_section.find('p') 
    else :
        p_tag=soup.find('p')
    return p_tag.get_text(strip=True) if p_tag else ''
def extract_page_data(html,page_url):
    return{
      'url':page_url,
      'h1':get_html_h1(html),
      'first paragraph':get_html_p(html),
    }
