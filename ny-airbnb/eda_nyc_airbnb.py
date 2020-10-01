import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 

#load data
nyc_df = pd.read_csv("AB_NYC_2019.csv")

#summary
print("Rows     :",nyc_df.shape[0])
print("Columns  :",nyc_df.shape[1])
print("\nFeatures :\n",nyc_df.columns.tolist())
print("\nMissing Value    :",nyc_df.isnull().sum().sum())
print("\nColumns with missing value:\n",nyc_df.isnull().any())

#drop unnecessary columns
nyc_df.drop(['id','name','host_name','last_review'], axis=1, inplace=True)
print(nyc_df.head())

#replacing all NaN values in 'reviews_per_month' with 0
nyc_df.reviews_per_month.fillna(0, inplace=True)
print(nyc_df.isnull().any())
