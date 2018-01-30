library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

stats <- c("Adv", "Per36","Per100P","PerGame","Totals")
years <- c("2011", "2012", "2013", "2014", "2015", 
           "2016", "2017")
fixYear <- function(year) {
  for (stat in stats) {
    tableName <- paste("~/Desktop/NBA-FA-SAGB/player-data/player",
                       year, "/",stat,"-", year,".csv", sep = "")
    # Unwrangled Player Salary table location
    table <- read.csv(tableName)
    fixName<- mutate(table, 
                     fix = gsub(
                       '[^A-Za-z]+', '',
                       gsub('[.]','',
                            tolower(
                              gsub('\\\\.*', '', Player)))))
    movedPlayers <- fixName %>%
      filter(Tm == "TOT")
    temp <- fixName %>% group_by(Player) %>%
      filter(max(row_number()) == 1) %>% ungroup()
    final <- rbind(temp, movedPlayers)
    
    printName <- paste(
      "~/Desktop/NBA-FA-SAGB/player-data-wrangled/player",
      year, "/",stat,"-",year,"wrangled.csv", sep = "")
    dir.create(paste("~/Desktop/NBA-FA-SAGB/player-data-wrangled/player",
      year, "/", sep = ""), showWarnings = FALSE)
    # Writes new wrangled tables in separate directory
    write.csv(final, file = printName, append = FALSE, sep = ",")
  }
}

for (year in years) {
  fixYear(year)
}


