setwd("E:/DATA 712")

data <- read.csv("712 Assignment 2 Data.csv")

#recoding missing variables as NA
data$USCITZN <- ifelse(data$USCITZN == 0, NA, data$USCITZN)
data$USCITZN <- ifelse(data$USCITZN >= 8, NA, data$USCITZN)

#recoding variable as binary (0, 1)
data$USCITZN <- ifelse(data$USCITZN >= 3, 1, data$USCITZN)
data$USCITZN <- ifelse(data$USCITZN == 2, 0, data$USCITZN)
data$USCITZN <- factor(data$USCITZN, ordered = F)
summary(data$USCITZN)
