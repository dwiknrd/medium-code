from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


url = "http://facebook.com"
# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path='/Users/macbook/Desktop/geckodriver/geckodriver')
driver.implicitly_wait(30)
driver.get(url)