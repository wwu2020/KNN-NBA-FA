library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

years <- c("2014", "2015", 
           "2016", "2017")

capNumber <- function(year) {
  if (year == "2011") {
    return(58044000)
  } else if (year == "2012") {
    return(58044000)
  } else if (year == "2013") {
    return(58679000)
  } else if (year == "2014") {
    return(63065000)
  } else if (year == "2015") {
    return(70000000)
  } else if (year == "2016") {
    return(94143000)
  } else {
    return(99093000)
  }
}

clusters <- function(salary) {
  if (salary < 800000) {
    return(1)
  } else if (salary < 1500000) {
    return(2)
  } else if (salary < 3000000) {
    return(3)
  } else if (salary < 5000000) {
    return(4)
  } else if (salary < 8000000) {
    return(5)
  } else if (salary < 10000000) {
    return(6)
  } else if (salary < 12500000) {
    return(7)
  } else if (salary < 15000000) {
    return(8)
  } else if (salary < 18000000) {
    return(9)
  } else {
    return(10)
  }
}

capClusters <- function(salary) {
  if (salary < .02) {
    return(1)
  } else if (salary < .04) {
    return(2)
  } else if (salary < .07) {
    return(3)
  } else if (salary < .1) {
    return(4)
  } else if (salary < .13) {
    return(5)
  } else if (salary < .16) {
    return(6)
  } else if (salary < .19) {
    return(7)
  } else {
    return(8)
  }
}

wrangleSet <- function(year) {
  salName <- paste("~/Desktop/NBA-FA-SAGB/salary-data/fa-salary-corrected/",
                   year, ".csv", sep = "")
  # Location of NBA FA salaries
  statName <- paste("~/Desktop/NBA-FA-SAGB/standardized-data/", year,".csv", sep = "")
  # Location of standarized player statistics
  sal <- read.csv(salName, stringsAsFactors = FALSE)
  stat <-read.csv(statName, stringsAsFactors = FALSE)
  
  salary <- sal %>% select(average.salary, name)
  data <- stat %>% inner_join(sal, c("fix" = "name"))
  cap <- capNumber(year)
  
  final <- data %>% select(name = fix, DRB, TOV, PPG = PS.G, VORP, Salary = average.salary) %>%
    filter(Salary >= 300000) %>% mutate(PercentCap = Salary/cap)
  # %>% mutate_each_(funs(scale(.) %>% as.vector), vars=c("Salary"))
  
  final <- final %>% mutate(Cluster = sapply(Salary, clusters),
                            capCluster = sapply(PercentCap, capClusters))
  
  final
  
  return(final)
}


data2014 <- wrangleSet("2014")
data2015 <- wrangleSet("2015")
data2016 <- wrangleSet("2016")
data2017 <- wrangleSet("2017")

final <- rbind(data2014,
               data2015, data2016, data2017)

write.csv(final, "TrainingSet.csv")
# Output location
