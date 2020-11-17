#import library
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

pages = [1]
for page in pages:
    url = "https://shopee.sg/Men's-Shoes-cat.168?page={}".format(page)
    driver = webdriver.Firefox(executable_path='/Users/macbook/Desktop/geckodriver/geckodriver')
    driver.implicitly_wait(30)
    driver.get(url)
    y = 1000
    for timer in range(0,20):
         driver.execute_script("window.scrollTo(0, "+str(y)+")")
         y += 1000  
         time.sleep(1)


    soup = BeautifulSoup(driver.page_source, "lxml")

    shoes = soup.find_all("div", "_1gkBDw")
    

    product_name = []
    product_price = []

    for shoe in shoes:
        name = shoe.find("div", "O6wiAW").text
        price = shoe.find("span", "_341bF0").text
        product_name.append(name)
        product_price.append(price)
        

    product = {"name": product_name, "price": product_price}
    product_df = pd.DataFrame(product, columns = ["name","price"])

    product_df.to_csv("men_shoes.csv")

    driver.close()

