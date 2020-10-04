import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 

#load data
nyc_df = pd.read_csv("AB_NYC_2019.csv")

#summary
# print("Rows     :",nyc_df.shape[0])
# print("Columns  :",nyc_df.shape[1])
# print("\nFeatures :\n",nyc_df.columns.tolist())
# print("\nMissing Value    :",nyc_df.isnull().sum().sum())
# print("\nColumns with missing value:\n",nyc_df.isnull().any())

#drop unnecessary columns
nyc_df.drop(['id','name','host_name','last_review'], axis=1, inplace=True)
print(nyc_df.head())

#replacing all NaN values in 'reviews_per_month' with 0
nyc_df.reviews_per_month.fillna(0, inplace=True)
print(nyc_df.isnull().any())

# #Neighbourhood Group
# plt.style.use('fivethirtyeight')
# plt.figure(figsize=(13,7))
# plt.title("Neighbourhood Group")
# g = plt.pie(nyc_df.neighbourhood_group.value_counts(), labels=nyc_df.neighbourhood_group.value_counts().index,autopct='%1.1f%%', startangle=180)
# plt.show()

# #Map of neighbourhood group
# plt.figure(figsize=(13,7))
# plt.title("Map of Neighbourhood Group")
# sns.scatterplot(nyc_df.longitude,nyc_df.latitude,hue=nyc_df.neighbourhood_group)
# plt.ioff()
# plt.show()

# #Room type
# plt.figure(figsize=(13,7))
# plt.title("Type of Room")
# sns.countplot(nyc_df.room_type, palette="muted")
# fig = plt.gcf()
# plt.show()

# plt.figure(figsize=(13,7))
# plt.title("Room Type on Neighbourhood Group")
# sns.countplot(nyc_df.neighbourhood_group,hue=nyc_df.room_type, palette="muted")
# plt.show()

# #Neighbourhood Group vs. Availability Room
# plt.style.use('classic')
# plt.figure(figsize=(13,7))
# plt.title("Neighbourhood Group vs. Availability Room")
# sns.boxplot(data=nyc_df, x='neighbourhood_group',y='availability_365',palette="dark")
# plt.show()

# #Neighbourhood Group Price Distribution
# #Price Varies vs. Area
# plt.figure(figsize=(13,7))
# plt.title("Map of Price Distribution")
# ax=nyc_df[nyc_df.price<500].plot(kind='scatter', x='longitude',y='latitude',label='availability_365',c='price',cmap=plt.get_cmap('jet'),colorbar=True,alpha=0.4)
# ax.legend()
# plt.ioff()
# plt.show()

# plt.style.use('classic')
# plt.figure(figsize=(13,7))
# plt.title("Neighbourhood Group Price Distribution < 500")
# sns.boxplot(y="price",x ='neighbourhood_group' ,data = nyc_df[nyc_df.price<500])
# plt.show()

# #correlation
# corr = nyc_df.corr(method='kendall')
# plt.figure(figsize=(13,10))
# plt.title("Correlation Between Different Variables\n")
# sns.heatmap(corr, annot=True)
# plt.show()

#prediction
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn import preprocessing
from sklearn.feature_selection import RFE

import warnings 
warnings.filterwarnings('ignore')