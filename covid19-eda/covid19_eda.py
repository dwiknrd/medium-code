import json
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import datetime

#create API function
def get_json(api_url):
	response = requests.get(api_url)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

#called api function
record_date = '2020-08-17'
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
##1. Cases in continent

##2. Fatality Ratio
#add "fatality_ratio" featured
df_covid_denormalized['fatality_ratio'] = df_covid_denormalized['deaths']/df_covid_denormalized['cases']
#top 20 country high fatality
df_top_20_fatality_rate = df_covid_denormalized.sort_values(by='fatality_ratio', ascending=False).head(20)


##3. 

