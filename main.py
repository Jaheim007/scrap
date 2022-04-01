from cgitb import html
from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read() 
f.close()

soup = BeautifulSoup(html_content, "html.parser")
title = soup.find("h1")
paragragh = soup.find(class_ = "description")
div_image = soup.find("div", class_= "info")
img_ing = div_image.find("img")

print(title.text)
print(paragragh.text)
print(img_ing["src"])