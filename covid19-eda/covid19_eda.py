import json
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import datetime

import plotly.graph_objects as go
from plotly.subplots import make_subplots

#create API function
def get_json(api_url):
	response = requests.get(api_url)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

#called api function
record_date = '2020-10-12'
covid_url = 'https://covid19-api.org/api/status?date='+record_date
df_covid_worldwide = pd.io.json.json_normalize(get_json(covid_url))

#clensing
df_covid_worldwide['last_update'] = pd.to_datetime(df_covid_worldwide['last_update'], format='%Y-%m-%d %H:%M:%S')
df_covid_worldwide['last_update'] = df_covid_worldwide['last_update'].apply(lambda x: x.date())

#new dataframes countries
countries_url = 'https://covid19-api.org/api/countries'
df_countries = pd.io.json.json_normalize(get_json(countries_url))
df_countries = df_countries.rename(columns={'alpha2': 'country'})[['name','country']]

#merge df_covid_worldwide and df_countries
df_covid_denormalized = pd.merge(df_covid_worldwide, df_countries, on='country')

#drop unnecessarry collumns

#EDA


##1. Fatality Ratio
#add "fatality_ratio" featured
df_covid_denormalized['fatality_ratio'] = round((df_covid_denormalized['deaths']/df_covid_denormalized['cases'])*100,2)
#top 20 country high fatality
df_top_20_fatality_rate = df_covid_denormalized.sort_values(by='fatality_ratio', ascending=False).head(20)

#visualisation

plt.figure(figsize=(17, 7))
plt.style.use('fivethirtyeight')
y = df_top_20_fatality_rate['name']
x = df_top_20_fatality_rate['fatality_ratio']
plt.ylabel('Country Name')
plt.xlabel('Fatality Rate')
plt.title('Top 20 Highest Fatality Rate Countries')
plt.xticks(rotation=45)
plt.hlines(y=y, xmin=0, xmax=x, color='indianred', alpha=0.8, linewidth=10)
plt.plot(x, y, "o", markersize=8, color='#007acc', alpha=0.8)
plt.tight_layout()
plt.show()

##2. Cases in continent
countries_df = pd.read_csv("countries.csv")
countries_df = countries_df.rename(columns = {'location': 'name'}, inplace = False)

covid_df = countries_df.merge(df_covid_denormalized, on='name')

continent_case = covid_df.groupby('continent')['cases'].sum()
plt.figure(figsize=(13,7))
plt.title("Percentage of Confirmed Cases on Each Continent")
g = plt.pie(continent_case, labels=continent_case.index,autopct='%1.1f%%', startangle=180)
plt.show()

##3. Mortality Rate

covid_df["mortality_rate"] = round((covid_df['deaths']/covid_df['population'])*100,2)
covid_mortality_top_20 = covid_df.sort_values(by='mortality_rate', ascending=False).head(20)

plt.figure(figsize=(17, 7))
y = covid_mortality_top_20['name']
x = covid_mortality_top_20['mortality_rate']
plt.ylabel('Country Name')
plt.xlabel('Mortality Rate')
plt.title('Top 20 Highest Fatality Rate Countries')
plt.xticks(rotation=45)
plt.hlines(y=y, xmin=0, xmax=x, color='darkblue', alpha=0.8, linewidth=10)
plt.plot(x, y, "o", markersize=8, color='#007acc', alpha=0.8)
plt.tight_layout()
plt.show()