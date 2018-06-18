import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

file = open('amz.csv', 'w')
writer = csv.writer(file)

headers = {'User-Agent': 'Mozilla/5.0'}

# inputs 	
shirt = "B01BXGKDD8"

toWrite = []

	
url = "https://www.amazon.com/"+"dp/"+shirt
print ("Processing: "+url)
page = requests.get(url,headers=headers)
bsobj = BeautifulSoup(page.content, "html.parser")

myShirt = bsobj.find("span", id="productTitle")
myShirt = myShirt.get_text().strip()
# print(myShirt)
# print(myShirt.get_text().strip())
myPrice = bsobj.find("span", id="priceblock_ourprice")
myPrice = myPrice.get_text()
myPrice = float(myPrice[1:5])
# print(myPrice)

car = bsobj.find("div", class_="a-carousel-col a-carousel-center")
# print(car)
eachProduct = car.findAll("div", class_="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4")
eachProduct = [p.get_text().strip() for p in eachProduct]
# for i in eachProduct:
# 	i = filter(lambda ch: ch not in ",", i)


prices = bsobj.findAll("span", class_="p13n-sc-price")
prices = [p.get_text().strip() for p in prices]
prices = [float(p[1:5]) for p in prices]

writer.writerow(eachProduct)
writer.writerow(prices)

# # toWrite.extend(myShirt)
# toWrite.extend(eachProduct)
# # toWrite.extend(myPrice)
# toWrite.extend(prices)

# print(toWrite)
# file.write(toWrite)

# print(prices)
comp = zip(eachProduct, prices)

deal = [p for p in comp if p[1] < myPrice]

sleep

file.close()







