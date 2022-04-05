from bs4 import BeautifulSoup
import requests

url = 'https://just-scrape-it.com/collections/hoodie-sweat'
url1 = 'https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt'
url2 = 'https://just-scrape-it.com/collections/gants'
url3 = 'https://just-scrape-it.com/collections/maillots-ete'
url4 = 'https://just-scrape-it.com/collections/stickers' 

source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

# price = soup.find("div", class_="page-width").find("ul")
# text = list(price.descendants)
# print(text)
# for il in price.find_all("li"):     
#     print(il)

price = soup.find('ul', class_='grid grid--uniform grid--view-items')
prix = soup.find_all('li', class_ = 'grid__item grid__item--collection-template small--one-half medium-up--one-quarter')
map = soup.find_all('div', class_ = 'price__regular')

for deals in prix:
    print(deals.span.text)

for m in map:       
    print(m.dd.text)

for d in prix:     
    print(d.img["src"])

    
    # print(first_item)
       
  

       
       
    
    



# print(price.text)
# print(deal)
# print(prix.text)

# for i in soup.find('ul', class_='grid grid--uniform grid--view-items'):        
#     if price.find('span', class_='price-item price-item--regular') == "Épuisé":     
#         print("Good Job")
#     else:     
#         print("Not Good")
