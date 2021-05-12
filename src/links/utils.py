import requests
from bs4 import BeautifulSoup
import lxml
#url= "https://www.amazon.com/PlayStation-VR-Marvels-Iron-Bundle-4/dp/B08CD34NZH/ref=sr_1_1?crid=2OXO95PIIYSF&dchild=1&keywords=playstation+vr+-+marvel%27s+iron+man+bundle&qid=1619339713&sprefix=playsation+vr+-+m%2Caps%2C268&sr=8-1"
#url= "https://www.amazon.com/dp/B08F7PTF53/"
url= "https://www.amazon.com/FIFA-21-Xbox-One-X/dp/B089F479ZR/ref=sr_1_1?dchild=1&keywords=FIFA+21%28X+box+one%29&qid=1619339809&sr=8-1"


def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)
    soup= BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price
print(get_link_data(url))

