from bs4 import BeautifulSoup
import requests

url = 'https://just-scrape-it.com/collections/hoodie-sweat'

source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

# price = soup.find("div", class_="page-width").find("ul")
# text = list(price.descendants)
# print(text)
# for il in price.find_all("li"):     
#     print(il)

price = soup.find('ul', class_ = "grid grid--uniform grid--view-items")
deal = price.find()

print(price.text)

# for i in soup.find('ul', class_='grid grid--uniform grid--view-items'):        
#     if price.find('span', class_='price-item price-item--regular') == "Épuisé":     
#         print("Good Job")
#     else:     
#         print("Not Good")
