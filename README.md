# K2Project2 - NFL Stadium Arrests - EDA

### Introduction

This is an open-ended Exploratory Data Analysis project for the Data Science program at K2 Data Science. 

### About

It’s football season!! With the 2018 season set to begin on September 6, 2018, I’m interested in looking at the public records of police arrests at NFL stadiums. Can stadium staff know when they need to request more police? Do states with higher alcohol consumption per capita (aged over 21) suggest a higher number of arrests?

### Goals

Evaluate public records of police arrests at NFL stadiums and alcohol consumption for each US state to determine if there is a trend or a factor that indicates a high number of arrests.

### Initial Reserach Findings

The count of arrests for each year is similar, with no trend. 

### Further Research & Analysis

### Assumptions



### Approach

The stadium arrests data was acquired from kaggle. The data contained arrests from 2011 - 2015 of public police records of arrests made at NFL stadiums. Note this dataset predates the recent moves by the Chargers, Rams, and Raiders.

To aid in my analysis, data on per capita alcohol consumption by State and type of alcoholic beverage for the years from 1970 - 2016 was acquired from The National Institute on Alcohol Abuse and Alcoholism (Surveillance Report #110). For consistency, my analysis only contains data from years 2011 - 2015. 

### Cleaning and Exploring Data

The stadium arrests data contained attributes for the season (year), week number, day of the week, and time the game occurred.  It further details the home team and away team, and the respective final scores. Finally, the data contains the number of arrests made at the game and categorical variables for if there was overtime and if it was a division game. 

To analyze the dataset more, I created dummy variables for OT_flag and for whether or not the home team won. Additionally, I created variables for the hour of the game time and the absolute difference of the final score. 

Out of curiousity, I wanted to know the home team with the most arrests in aggregate over the entire dataset (2011 to 2015 seasons). I hypothesized that it would be the Oakland Raiders, because the fans are notoriously obnoxious and have a bad reputation for being disrepectful. I was surprised to see that Oakland only ranked 5th (658), behind San Deigo Chargers (983), NY Giants, NY Jets, and Pittsburgh Steelers, with San Diego ranked 1st. However, Oakland was ranked #2 (321) in the overall arrests as the away team, behind the Dallas Cowboys (328). Finally, a bit less surprising after the overall ranks, the highest overall arrests for a match up was the San Diego Chargers and the Oakland Raiders (197). 

Next, I wanted to see which variables in the dataset has a statistically significant relationship with the number of arrests. I performed a simple linear regression on the variables OT, game_result, game_hour, and score_diff, individually, against the dependent variable arrests. The regressions determined that only game_result and game_hour are statistically significant, with p-values 0.0275 of 4.70e-06, respectively. 

Looking at the hours of when the games started, it suggests that an increase in an hour of game start time (aka later in the day) increases the expected number of arrests by 0.5382
