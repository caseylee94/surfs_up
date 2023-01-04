# surfs_up

## Challenge Overview

The purpose of this challenge is to determine the feasibility of opening an ice cream and surf shop in Oahu, Hawaii based on year-round weather data. It is important to the main investor, W. Avy, to look deeply into the weather patterns because weather is an integral part of the success of both of these business ventures. The data-driven decisions that will be determined are based on temperature for the past 7 years from 2010-2017, specifically June and December. These 2 months are far apart enough to ensure there are good conditions year-round.

## FEATURES AND DATA SOURCES

* Data Source: hawaii.sqlite
* Programming Files: SurfsUp_Challenge.ipynb, climate_analysis.ipynb
* Data Tools: Python SQL toolkit (SQLAlchemy), Object Relational Mapper, pandas, numpy
* Software: SQLlite, Python 3.9.2, Flask, Jupyter Notebook

## Results

The summary statistics for temperature for each month were found using Python pandas libray. The results for the month of June are shown below:

 ![June_Temps.png](/Resources/June_Temps.png)
 
 The same analysis was performed for the month of December and are shown below:
 
  ![December_Temps.png](/Resources/December_Temps.png)

* The average temperature for June is 75F and the average temperature for December is 5% lower at 71F
* The December temperatures seem to be more variable than those in June given its larger range in recorded temperatures (comparing the max vs min temp of each month)
* The minimum temperature in December will have the biggest impact on the business at 56F

To assist potential investors that are unfamiliar with Jupyter Notebook and VSCode, a Flask App was created to allow them to view the results of the temperature data in a user-friendly interface. The app shows users the precipitation data, the stations data, and the temperature observations. The app also allows users to choose a start and end data and then see the minimum, maximum, and average temperatures for that range.

## Summary 

Even though the temperatures in December have a wider range and are overall lower than June, the difference is not so drastic that it would hurt the business enough to make it not feasible. The average temperatures for the months are close together with only a 5% difference across the six months. The ice cream sales would be more affected than the surf business on the particularly colder days, especially if the temperature drops into the 50Fs. The business could choose to stock less ice cream during the winter months to help cut down on losses this may cause. I recommend additional queries for the months of September and March to ensure there are no drastic differences during the spring and fall. Further analysis of rainfall data during these months would be beneficial, especially looking at the spring months. I highly recommend running deep analysis on the wind conditions for all four seasons, as these contribute the most to the surfing business as well as wave conditions. Temperature in my opinion mostly affects the ice cream sales as it will affect the average beach goers the most. Overall, so far looking at the data it is looking very feasbile to invest in this business.
