library(httr)
library(dplyr)
library(ggplot2)
library(hrbrthemes)

resp <- GET("https://data.covid19.go.id/public/api/update.json")
#header
headers(resp)

#extraction
covid_raw <- content(resp, as = "parsed", simplifyVector = TRUE) 
str(covid_raw)
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
covid_update$total$jumlah_sembuh

covid_days <- covid_update$harian
str(covid_days)
new_covid_df <-
  covid_days %>% 
  select(-contains("key_as_string")) %>% 
  select(-contains("doc_count")) %>%
  select(-contains("jumlah_positif_kum")) %>% 
  select(-contains("jumlah_sembuh_kum")) %>%
  select(-contains("jumlah_meninggal_kum")) %>%
  select(-contains("jumlah_dirawat_kum")) %>%
  select(-contains("jumlah_dirawat")) %>%
  rename(
    date = key,
    deaths = jumlah_meninggal,
    healed = jumlah_sembuh,
    cases = jumlah_positif
  ) %>% 
  mutate(
    date = as.POSIXct(date / 1000, origin = "1970-01-01"),
    date = as.Date(date)
  )
head(new_covid_df)

ggplot(new_covid_df, aes(date, cases$value)) +
  geom_col(fill = "salmon") +
  labs(
    x = NULL,
    y = "Total Cases",
    title = "Total Cases COVID-19 in Indonesia",
    caption = "Source: covid.19.go.id"
  ) +
  theme(plot.title.position = "plot")



