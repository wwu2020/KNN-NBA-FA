library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

stats <- c("Adv", "PerGame")
years <- c("2018")
fixYear <- function(year) {
  for (stat in stats) {
    tableName <- paste("~/Desktop/NBA-FA-SAGB/2018-Predictions/",
                       stat, year,".csv", sep = "")
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
      "~/Desktop/NBA-FA-SAGB/2018-Predictions/",
     stat,"-", year, "wrangled.csv", sep = "")
    
    
    write.csv(final, file = printName, append = FALSE, sep = ",")
  }
}

for (year in years) {
  fixYear(year)
}


