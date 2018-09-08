# K2Project2 - NFL Stadium Arrests - EDA

### Introduction

This is an open-ended Exploratory Data Analysis project for the Data Science program at K2 Data Science. 

### About

It’s football season!! With the 2018 season set to begin on September 6, 2018, I’m interested in looking at the public records of police arrests at NFL stadiums. Can stadium staff know when they need to request more police? Do states with higher alcohol consumption per capita (aged over 21) suggest a higher number of arrests?

### Goals

Evaluate public records of police arrests at NFL stadiums and alcohol consumption for each US state to determine if there is a trend or a factor that indicates a high number of arrests.

### Initial Reserach Findings

The count of arrests for each year is similar, with no trend. 

![Arrests Per Year](https://github.com/lalitayang/K2Project2/blob/master/images/arrestsPerYear.png)

### Assumptions
I am assuming that there are the same number of attendees at each of the football games so that the number of arrests is normalized.

### Approach

The stadium arrests data was acquired from kaggle. The data contained arrests from 2011 - 2015 of public police records of arrests made at NFL stadiums. Note this dataset predates the recent moves by the Chargers, Rams, and Raiders.

To aid in my analysis, data on per capita alcohol consumption by State and type of alcoholic beverage for the years from 1970 - 2016 was acquired from The National Institute on Alcohol Abuse and Alcoholism (Surveillance Report #110). For consistency, my analysis only contains data from years 2011 - 2015. 

After the datasets were cleaned, they were left joined on stadium arrests to analyize the relationship.

### Conclusion

While the datasets were interesting and I was surprised to see that Oakland did not have the most arrests, I did not find any strong or practical correlations or between any variables of the Stadium Arrests dataset or the Alcohol Consumption dataset, except when the game starts. Games that start later in the day tends to have a higher number of arrests. As such, stadium staff could hire more police for night games, however the number of arrest does not increase significantly as it gets later in the day (1 more arrest for every 2 hours later).
