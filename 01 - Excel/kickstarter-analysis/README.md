# Kickstarting with Excel

## Overview of Project
Louise is wanting to start a crowdfunding campaign to help fund her play *Fever*.  She has compiled data of other crowdfunding compaigns with information such as when the campaign launched, ended, what the goals were, and whether or not those campaigns were successful in meeting their goal.  

### Purpose
Louise wants this information analyzed and presented so that she can make an informed decision on the best time to start her campaign and whether her goal of $10,000 may result in a successful campaign.

## Analysis and Challenges
Two analyses were requested: one based on outcomes relative to launch date for theater campaigns, and one based on outcomes relative to initial funding goals for the campaigns just for plays.

### Analysis of Outcomes Based on Launch Date
A pivot table was created using the data provided, filtered by the Parent Category "theater" and by years.  Outcomes were split by the month of each launch date and whether each campaign was succeessful, failed, or canceled.  Finally, a line graph was created showing outcomes based on the month of launch date.

![Theater_Outcomes_vs_Launch](https://user-images.githubusercontent.com/106561880/173205120-58107619-11f7-45b8-b179-1a4aa151b293.png)



### Analysis of Outcomes Based on Goals
On a new table, goal amounts were grouped into ascending ranges, from less than $1000, up to $50,000 or more.  Then, each number of successful, failed, and canceled for campaigns of plays were tallied, totaled, and given a percentage based on total.  Finally, a line graph was created showing how campaigns fared within each of these ranges.

![Outcomes_vs_Goals](https://user-images.githubusercontent.com/106561880/173205158-ea0114b1-8481-4404-b422-bbabca0a8e93.png)


### Challenges and Difficulties Encountered
Since goals were originally listed as specific dollar amounts and not ranges, a new table had to be created so that this information could more easily be summarized.
## Results

- Based on these findings, Louise should start her campaign in May, and a $10,000 goal has a greater likelihood of success than failure.

- From Outcomes Based on Launch Date, it can be concluded that most successful campaigns start in May.  Also, the least successful campaigns started in December, with very little variance of successful vs. failed campaigns. 

- From Outcomes Based on Goals, it can be concluded that the likelihood of success decreases as goal amounts increase.  Up to the $15,000 - $20,000 range, there were more successful campaigns vs. failed campaigns.

- This data is limited by the fact that there are fewer campaigns with goals larger than $15,000.  This results in a less reliable dataset as goal amounts increase.  There also is not data that shows how much money was spent or which methods were employed in marketing each campaign.

- Without additional data to show which resources were used to market each campaign, it can be theorized that the number of backers and average donation could relate to how well each campaign was marketed.  Another useful table or chart could show Outcomes Based on Number of Backers and/or Average Donation.
