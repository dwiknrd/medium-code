#import library
import pandas as pd
import dryscrape
from bs4 import BeautifulSoup

dryscrape.start_xvfb()
pages = range(1,2)
for page in pages:
    url = "https://shopee.co.id/Sepatu-Pria-cat.35?page={}".format(page)
    session = dryscrape.Session(base_url = 'http://google.com')
    # html = session.visit(url)
    # response = session.body()
    # soup = BeautifulSoup(response)
    # print(soup)
    # print("halooww")
    #shoes = soup.find_all("div", "col-xs-2-4 shopee-search-item-result__item")
    # print(len(shoes))

    # for shoe in shoes:
    #     name = shoe.find("div", "_1NoI8_ _16BAGk").text
    #     price = shoe.find("span", "_341bF0").text

    #     print(name)
    #     print(price)

