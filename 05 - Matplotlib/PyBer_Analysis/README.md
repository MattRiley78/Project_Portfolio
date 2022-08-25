# PyBer_Analysis
## Project Overview
After routine analysis of ride-share data from January 2019 - early May 2019, PyBer is requesting analysis and summarization of ride-share data by city type, as well as a visualization of the total weekly fares by city type.  This new analysis will exclude rides captured after 4/28/2019.  This analysis showing the differences by city type will aid PyBer in decision-making.

## Results

The summary from all data from January - early May 2019 shows noticeable trends between city types.

- As expected, there are fewer Total Rides and Total Drivers in less populated city types, most notably in Rural cities.
- Also as expected, the Total Fares for larger city types tend to be larger, due to the larger number of rides.
- The **ratio** of rides to drivers trends smaller in larger city types, meaning there are more drivers than rides in Urban markets.   
- The Average Fare per Ride and Average Fare per Driver also trend upward in less populated city types.

![SummaryDF](https://user-images.githubusercontent.com/106561880/178165497-7691ba25-723c-4cbf-b61c-07cea70cbcb4.png)

The weekly analysis shows that the total fares never cross lines.  It follows the general trend of Total Fares increasing by population size.  Weekly totals in Rural markets never exceed $500.  Weekly totals in Suburban markets range from $750 to $1500.  Weekly totals in Urban markets range from $1600 to nearly $2500.
![PyBer_fare_summary](https://user-images.githubusercontent.com/106561880/178165523-8b925cd3-a4b5-45d6-85c6-4e4ba56f12b5.png)

## Summary and Recommendations
Based on this analysis, it appears that drivers are attracted to Urban markets based on the idea that there is more money to be made in Urban markets.  However, the Average Fares are smaller in more populated markets.  This is because trips are generally shorter.  Average fares are higher in Rural Markets likely because riders are taking longer trips into more populated areas.  Urban drivers may not be aware of the greater average fares of Rural Rides.  Also, with fewer drivers, potential riders in Rural markets may not use the App because they feel like they may not get a ride.

1. A notification on the Driver App could be added that can tell Urban Drivers that there is a need for drivers in nearby Rural cities.  Also, a general message to Urban drivers as they open their app could pop up before they start their day to let them know that average fares per ride in Rural cities tend to be higher.  Then, they could check an option to pick up riders from nearby Rural cities.  Having some Urban drivers start pickups in nearby Rural cities can help balance out the ratios between the two city types.

2. A further cash bonus could be implemented to incentivize Urban Drivers to pick up from Rural cities.  On top of the increased fare, they would receive an additional bonus if they receive a Rural ride request while the driver is still in an Urban or Suburban area.  The bonus may be based on the distance the driver may drive to the pickup location.  This also may increase total fares for Rural cities.

3. A "return trip" function could be added to the Rider App for Rural riders who took a ride into a Suburban or Urban city and need a ride back home.  This function could also allow the rider to pick their original driver, if available.  This could also be an additional incentive for Drivers since they could earn the larger average fare for both trips.  This may also establish rapport between drivers and riders, where some riders may want to request certain drivers.

    Since these are Rural users, then a "return trip" from an Urban or Suburban market would count as a Rural Fare.  This may increase the Rider's feeling of reliability from our service and will more likely use the service again.  Hopefully, this will gain additional riders with word-of-mouth in Rural cities.  Ultimately, the goal is to increase the number of rides and revenue from Rural cities, as well as improve the ratio of rides to drivers between Urban and Rural markets.
 
