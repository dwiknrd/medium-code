import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_style("darkgrid")
matplotlib.rcParams["font.size"] = 14
matplotlib.rcParams["figure.facecolor"] = '#00000000'

#loading the dataset
netflix_df = pd.read_csv("netflix_titles.csv")

#Data Cleaning

##Data with missing value
print(netflix_df.T.apply(lambda x: x.isnull().sum(), axis = 1))
##Handling missing value
netflix_df.director.fillna("No Director", inplace=True)
netflix_df.cast.fillna("No Cast", inplace=True)
netflix_df.country.fillna("Country Unavailable", inplace=True)
netflix_df.dropna(subset=["date_added", "rating"], inplace=True)

#Netflix Content By Type

#Amount of Content as a Function of Time

#Countries by the Amount of the Produces Content

#Top Directors on Netflix

#Top Genres on Netflix

#Amount of Content By Rating

#Top Actor on Netflix

#Movie Duration