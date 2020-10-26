#import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

#make request to the website
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Physics').text
soup = BeautifulSoup(website_url, 'lxml')

#take table with class named 'wikitable sortable'
my_table = soup.find('table', {'class':'wikitable sortable'})

#searh data


#make an empty list


# enter the data to the list



#make a dataframe and extrat to csv file