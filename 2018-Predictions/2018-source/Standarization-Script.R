library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)


years <- c("2018")

standardizeData <- function(year) {
  perName <- paste("~/Desktop/NBA-FA-SAGB/2018-Predictions/PerGame-", year,"wrangled.csv", sep = "")
  advName <- paste("~/Desktop/NBA-FA-SAGB/2018-Predictions/Adv-",
                   year, "wrangled.csv", sep = "")
  
  perGame <- read.csv(perName, stringsAsFactors = FALSE)
  adv <-read.csv(advName, stringsAsFactors = FALSE)
  
  perGame <- perGame %>% filter(MP >= 5, G >=5)
  
  chooseAdv<- adv[, c("Player", "VORP", "fix")]
  choosePer<- perGame[, c("Player", "Pos", "Age", "Tm", "DRB", "TOV", "PS.G")]
  
  full<- choosePer %>% inner_join(chooseAdv, by = 'Player')
  head(full)
  partiallyScaled <- full %>% 
    mutate_each_(funs(scale(.) %>% as.vector), vars=c("TOV","PS.G","VORP"))
  
  smalls <- partiallyScaled %>%
    filter(Pos == 'PG' | Pos == 'SG' | Pos == 'G'
           | Pos == 'PG-SG' | Pos == 'SG-PG') %>% 
    mutate_each_(funs(scale(.) %>% as.vector), vars=c("DRB"))
  forwards <- partiallyScaled %>%
    filter(Pos == 'SF' | Pos == 'PF' | Pos == 'F' |
             Pos == 'SG-SF' | Pos == 'SF-SG' | 
             Pos == 'SF-PF' |  Pos == 'PF-SF') %>% 
    mutate_each_(funs(scale(.) %>% as.vector), vars=c("DRB"))
  centers <- partiallyScaled %>%
    filter(Pos == 'C' | Pos == "PF-C" | Pos == "C-PF") %>% 
    mutate_each_(funs(scale(.) %>% as.vector), vars=c("DRB"))
  
  print(partiallyScaled %>%
          filter(!Pos %in% c('PG', 'SG', 'G', 'SF', "PF", "F", "C",
                             "PF-C", "PG-SG", "SG-PG", "SG-SF",
                             "SF-SG", "SF-PF", "PF-SF", "C-PF")))
  
  final <- rbind (smalls, forwards, centers)
  
  printName <- paste(
    "~/Desktop/NBA-FA-SAGB/2018-Predictions/standardized-data/", year, ".csv", sep = "")
  write.csv(final, file = printName, append = FALSE, sep = ",")
  
}

dir.create("~/Desktop/NBA-FA-SAGB/2018-Predictions/standardized-data/", showWarnings = FALSE)
for (year in years) {
  standardizeData(year)
}