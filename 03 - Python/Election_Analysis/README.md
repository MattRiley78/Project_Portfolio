# Election_Analysis

## Project overview
A Colorado Board of Elections employee originally required the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code

## Original Results
The original analysis of the election shows that:
1. There were 369,711 votes cast in the election.
2. The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
3. Each candidate's results were:
    - Charles Casper Stockham received 85,213 votes.
    - Diana DeGette received 272,892 votes.
    - Raymon Anthony Doane received 11,606 votes.
4. Each candidate's percentage of the votes were:
    - Charles Casper Stockham: 23.0%
    - Diana DeGette: 73.8%
    - Raymon Anthony Doane: 3.1%
5. The winner of the elections was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

![Original_Results](https://user-images.githubusercontent.com/106561880/176063827-cd6e4a3c-8e24-437a-afb6-f0f4ce97bc9f.png)

## Challenge Overview
Upon receiving these results, the election commission requested additional data to complete the audit.

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count.
3. The county with the highest turnout.
## Challenge Results
Additional analysis of the data shows:

1. Each county's voter turnout:
    - Jefferson County: 38,855 voters
    - Denver County: 306,055 voters
    - Arapahoe County: 24,801 voters
2. The percentage of votes from each county were:
    - Jefferson County: 10.5%
    - Denver County: 82.8%
    - Arapahoe County: 6.7%
3. County with the highest turnout:
    - Denver County

![Additional_Results](https://user-images.githubusercontent.com/106561880/176063859-dc5657dc-3d08-4b64-b986-4519c7f22e00.png)

## Challenge Summary
This script can be useful for auditing data in upcoming elections.  It is currently versatile enough to calculate the number of candidates, their count and percentage of the vote, the number of counties, and voter turnout.  

With this data, additional scripts can also be written to determine each candidate's percentage within each county.  This can be helpful in determining which candidates performed better in which counties.  Additionally, with the Ballot ID numbers also captured, script can be created to check for duplicate entries.  This will help eliminate duplicate entries or determine possible voter fraud.
