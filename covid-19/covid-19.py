import matplotlib.pyplot as plt
import pandas as pd 

countries_df = pd.read_csv("countries.csv")
covid_data_df = pd.read_csv("covid-countries-data.csv")

total_tests_missing = covid_data_df.total_tests.isna().sum()
print("The data for total tests is missing for {} countries.".format(int(total_tests_missing)))

#merged countries_df with covid_data_df
combined_df = countries_df.merge(covid_data_df, on='location')

combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']
combined_df['cases_per_million'] = combined_df['total_cases'] * 1e6 / combined_df['population']
combined_df['deaths_per_million'] = combined_df['total_deaths'] * 1e6 / combined_df['population']


#Create a dataframe with 10 countires that have highest number of tests per million people.
highest_tests_df = combined_df.sort_values(by= 'tests_per_million', ascending=False).head(10)
plt.figure(figsize=(20, 8))
x = highest_tests_df.location
y = highest_tests_df.tests_per_million
plt.bar(x,y)
plt.xlabel("Country")
plt.ylabel("Number of Tests Per Million")
plt.title("Top 10 Countries Highest Number of Tests per Million People")
plt.show()

#Create a dataframe with 10 countires that have highest number of positive cases per million people.
highest_cases_df = combined_df.sort_values(by= 'cases_per_million', ascending=False).head(10)
plt.figure(figsize=(20, 8))
x = highest_cases_df.location
y = highest_cases_df.cases_per_million
plt.bar(x,y)
plt.xlabel("Country")
plt.ylabel("Number of Positive Cases Per Million")
plt.title("Top 10 Countries Highest Number of Positive Cases per Million People")
plt.show()

#Create a dataframe with 10 countires that have highest number of deaths per million people.
highest_deaths_df = combined_df.sort_values(by= 'deaths_per_million', ascending=False).head(10)
plt.figure(figsize=(20, 8))
x = highest_deaths_df.location
y = highest_deaths_df.cases_per_million
plt.bar(x,y)
plt.xlabel("Country")
plt.ylabel("Number of Deaths Per Million")
plt.title("Top 10 Countries Highest Number of Deaths per Million People")
plt.show()

#(Optional) Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".

both_tests_cases = highest_tests_df.merge(highest_cases_df, on='location')

print('The number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million" is {}.'.format(both_tests_cases.shape[0]))

#Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". 
#Only consider countries with a population higher than 10 million while creating the list.

high_population = countries_df[countries_df["population"]>10000000]
print(high_population)

lowest_gdp = high_population.sort_values("gdp_per_capita").head(20)
plt.figure(figsize=(20, 8))
x = lowest_gdp.location
y = lowest_gdp.gdp_per_capita
plt.bar(x,y)
plt.xlabel("Country")
plt.ylabel("Number of GDP per Capita")
plt.title("Countries With Lowest GDP per Capita")
plt.show()

lowest_beds = high_population.sort_values("hospital_beds_per_thousand",).head(20)
plt.figure(figsize=(20, 8))
x = lowest_beds.location
y = lowest_beds.hospital_beds_per_thousand
plt.bar(x,y)
plt.xlabel("Country")
plt.ylabel("Number of Hospital Beds per Thousand")
plt.title("Countries with Lowest Hospital Beds")
plt.show()

countries_lowest_gdp_bed = lowest_gdp.merge(lowest_beds, on="location")

print('The number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population" is {}.'.format(countries_lowest_gdp_bed.shape[0]))

