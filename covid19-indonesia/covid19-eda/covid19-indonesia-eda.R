library(httr)
resp <- GET("https://data.covid19.go.id/public/api/update.json")
#header
headers(resp)

#extraction
covid_raw <- content(resp, as = "parsed", simplifyVector = TRUE) 
length(covid_raw)
names(covid_raw)
#extract with new variable
covid_update <- covid_raw$update

lapply(covid_update,names)
covid_update$penambahan$tanggal
covid_update$penambahan$jumlah_sembuh
covid_update$penambahan$jumlah_meninggal
covid_update$total$jumlah_positif
covid_update$total$jumlah_meninggal