library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

wrangleSet <- function(year) {
  salName <- "~/Desktop/NBA-FA-SAGB/2018-Predictions/2018.csv"
  statName <- "~/Desktop/NBA-FA-SAGB/2018-Predictions/standardized-data/2018.csv"
  
  sal <- read.csv(salName, stringsAsFactors = FALSE)
  stat <-read.csv(statName, stringsAsFactors = FALSE)
  
  salary <- sal %>% select(name)
  data <- stat %>% inner_join(sal, c("fix" = "name"))
  
  final <- data %>% select(Player, Pos, Age, Tm, name = fix, DRB, TOV, PPG = PS.G, VORP)
  # %>% mutate_each_(funs(scale(.) %>% as.vector), vars=c("Salary"))
  
  
  return(final)
}

final <- wrangleSet("2018")
head(final)

write.csv(final, "~/Desktop/NBA-FA-SAGB/2018-Predictions/2018-Final-detailed.csv")
