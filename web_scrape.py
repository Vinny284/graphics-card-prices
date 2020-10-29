import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

page = 1
max_pages = 2
frame = []
properties = ['Price', 'GPU', 'Core Clock', 'Boost Clock', 'CUDA Cores','Stream Processors',
              'Memory Size','Memory Type', 'Memory Interface','Thermal Design Power']

base_url = 'https://www.newegg.com/global/uk-en/p/pl?d=graphics&N=600030348%20101582767%20600494828%20600358543%20600007787%20600286741%20600007782%20600007779&PageSize=96'

# page loop
while page <= max_pages:
  
    url = base_url + '&page=' + str(page)
    
    # get container for each card
    page_request = urlopen(url)
    page_html = page_request.read()
    page_request.close()
    
    page_soup = soup(page_html, 'html.parser')
    
    # get container for all cards
    main_containers = page_soup.findAll('div', {'class': 'list-wrap'})
    containers = main_containers[0].findAll('div', {'class': 'item-cell'})
    
    
    # graphics card loop
    for container in containers:
        
        # get link for the card page
        link_container = container.findAll('a', {'class': 'item-title'})
        if len(link_container) > 0:
            link = link_container[0]['href'].replace(' ','')
            
            # get price
            price_container = container.findAll('li', {'class': 'price-current'})
            price = price_container[0].strong.text.strip() + price_container[0].sup.text.strip()
            specs = [price] 
            
            
            page_request = urlopen(link)
            page_html = page_request.read()
            page_request.close()
            
            page_soup = soup(page_html, "html.parser")
            
            # get container for specs
            specs_container = page_soup.findAll('dl')             
        
            
            # specifications loop
            for prop in properties[1:]:
                match = False
                for spec in specs_container:
                    label = spec.findAll('dt')[0].text
                    if prop == label:
                        match = True
                        value = spec.findAll('dd')[0].text
                
                if not match:
                    value ='NULL'
                    
                specs.append(value)
                       
            frame.append(specs)
        
    
    page += 1
    print('new page')

    
df = pd.DataFrame(frame, columns=properties)
df.to_csv('graphics_data2.csv', index=False)
   
