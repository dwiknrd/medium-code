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
from sklearn import metrics
from sklearn.metrics import mean_squared_error,r2_score, mean_absolute_error
from sklearn import preprocessing


import warnings 
warnings.filterwarnings('ignore')

#encode label with value between 0 and n_classes-1
encode = preprocessing.LabelEncoder()
#fit label encoder
encode.fit(nyc_df.neighbourhood_group)
nyc_df.neighbourhood_group=encode.transform(nyc_df.neighbourhood_group)

# Transform labels to normalized encoding
encode = preprocessing.LabelEncoder()
encode.fit(nyc_df.neighbourhood)
nyc_df.neighbourhood=encode.transform(nyc_df.neighbourhood)

encode = preprocessing.LabelEncoder()
encode.fit(nyc_df.room_type)
nyc_df.room_type=encode.transform(nyc_df.room_type)

nyc_df.sort_values(by='price',ascending=True,inplace=True)

# print(nyc_df.head(20))

#Train linier regression model

l_reg = LinearRegression()

X = nyc_df[['host_id','neighbourhood_group','neighbourhood','latitude','longitude','room_type','minimum_nights','number_of_reviews','reviews_per_month','calculated_host_listings_count','availability_365']]
y = nyc_df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

l_reg.fit(X_train,y_train)

#prediction

predicts = l_reg.predict(X_test)

print("Mean Squared Error: ", np.sqrt(metrics.mean_squared_error(y_test, predicts)))
print("R2 Score: ", r2_score(y_test,predicts) * 100)
print("Mean Absolute Error: ", mean_absolute_error(y_test,predicts))
print("Mean Squareroot Error: ", mean_squared_error(y_test,predicts))

#Actual Vs Predicted for Linear Regression
lr_pred_df = pd.DataFrame({
        'actual_values': np.array(y_test).flatten(),
        'predicted_values': predicts.flatten()}).head(20)

print(lr_pred_df.head(5))

x = lr_pred_df.index
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, lr_pred_df.actual_values, width, label='Actual Values')
rects2 = ax.bar(x + width/2, lr_pred_df.predicted_values, width, label='Predicted Values')
ax.set_ylabel('Price')
ax.set_title('Actual Vs Predicted for Linear Regression')
ax.set_xticks(x)
ax.legend()
fig.tight_layout()
plt.show()