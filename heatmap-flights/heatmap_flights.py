import seaborn as sns 

flights = sns.load_dataset("flights").pivot("month", "year", "passengers")