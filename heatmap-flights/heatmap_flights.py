import seaborn as sns 

flights = sns.load_dataset("flights").pivot("month", "year", "passengers")
sns.heatmap(flights)
sns.heatmap(flights, fmt="d", annot=True, cmap='Blues')
sns.heatmap(flights, fmt="d", cmap='YlGnBu')
sns.heatmap(flights, center=flights.loc["Jan", 1955])