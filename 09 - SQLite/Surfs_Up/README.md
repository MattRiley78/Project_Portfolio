# Surfs_Up
## Project Overview
My completed business plan to realize my dream of opening a "Surf & Shake" shop in Hawaii, where I can sell surfing equipment and ice cream treats, has attracted interested investor W. Avy.  Before he will commit to investing in this venture, he wants a weather analysis to determine if this would be profitable year-round.  More specifically, an analysis of temperature data from the months of June and December is requested to see if the temperatures are warm enough to sustain the business year-round.

## Methods
Data was pulled from a sqlite file with recorded weather data from January 2010 through August 2017.  Using SQLAlchemy and Jupyter Notebook, Exploratory Data Analysis was performed before producing the final analysis.

## Results
![June_Temps](https://user-images.githubusercontent.com/106561880/183270864-c6b75237-ad43-446c-ac73-61fbe5cacdba.png)
![December_Temps](https://user-images.githubusercontent.com/106561880/183270866-115f3e14-4d84-484d-9e63-da4bc7200a1e.png)

- The average temperature in June is almost 75°F, and the average temperature in December is about 71°F.
- The lowest recorded temperature in June was 64°F, and the lowest recorded tempearture in December was 56°F.
- The highest recorded temperature in June was 85°F, and the highest recorded tempearature in December was 83°F.



## Summary and Recommendations
As can be seen from this data, there is not much variance of temperatures between June and December.  Oahu is known for its year-round mild temperatures, and our analysis proves this.  Even during Winter months, the temperature is often warm enough for people to enjoy ice cream and surfing.

Additional data was also included in the sqlite file, including precipitation amounts and elevations.  Additional queries for precipitation amounts can account for the island's wettest months.  While some customers may like to surf in the rain, it can still put a damper on business, especially on ice cream sales.

Also, this data was filtered for all stations.  There are other stations throughout the island, including those with different elevations.  This can affect overall temperature readings.  This analysis could also be filtered by specific station(s) that would be closest to the actual shop site.  If we decide to open multiple stores on the island, we can also filter the queries by the closest stations to get the most accurate readings from that area.
