import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = requests.get("https://alphasquare.co.kr/home/stock/stock-summary?code=066570&gclid=CjwKCAjwi8iXBhBeEiwAKbUoffE2WexCo65EBhbJ_Es0p7ht4Mu7iI0rQfjJuUeCnkw2B4BP2sZLVxoCMtUQAvD_BwE")
bsObject = BeautifulSoup(html.content, "html.parser")

print(bsObject.h2)