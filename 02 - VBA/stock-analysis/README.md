# Green Energy Stocks Analysis with VBA

## Overview of Project
Steve's parents are wanting to invest in Green Energy and have requested information on stock DQ.  Steve is concerned about DQ stock and needs an analysis of other Green stocks so they can diversify their funds.  Steve has compiled stock data from 12 different Green stocks for two different years, including stock DQ.  This includes closing prices for each close date for each stock for both years.
 

### Purpose
Steve wants a summary of how each stock performed over each year, including the total annual volume for each stock and the percentage of return at the end of the year.

## Analysis and Challenges
Using VBA in Excel, a process was created to analyze all stocks.  While the code was more readable, it was discovered that the run time for the code was somewhat lengthy.  This could create problems if the same code is used to analyze a larger set of stocks.  Therefore, a refactored version of the same process was created.  

### All Stocks Analysis (Original)
VBA Code was written where the Stock Year is inputted to initiate the analysis.  A Timer is set to check the performance of the analysis.  With over 3,000 rows of data, the run time for each year is roughly 0.8 seconds.

![All_Stocks_2017_Original](https://user-images.githubusercontent.com/106561880/174915710-79c518cd-66ac-43a6-8214-506285c8d0f2.png)
![All_Stocks_2018_Original](https://user-images.githubusercontent.com/106561880/174915728-d7d980b0-c8e3-4207-95e1-d2bddc8b22a0.png)


### All Stocks Analysis (Refactored)
To decrease the run time, the AllStocksAnalysis VBA code was copied and refactored to make the subroutine more efficient.  Additional arrays and variables were created to reference within the code to avoid repetitive steps.  Refactored run times fell to less than 0.06 seconds.

![VBA_Challenge_2017](https://user-images.githubusercontent.com/106561880/174915743-4f35fc05-a99b-44c9-9bfd-743f1d77ef44.png)
![VBA_Challenge_2018](https://user-images.githubusercontent.com/106561880/174915748-c1b8cb65-c413-43e3-b8ac-0144f8065b5f.png)

### Challenges and Difficulties Encountered
Creating the refactored code eliminated the need for nested loops in this case.  However, in order to accomplish this, certain sections of the code had to be reordered or rewritten based on the new logic using additional variables and arrays.  New code had to go through more debugging in order to work properly.

## Results
![2017_Results](https://user-images.githubusercontent.com/106561880/174927924-c2739468-f837-4e70-b94a-1ded9caf2a36.png)
![2018_Results](https://user-images.githubusercontent.com/106561880/174927933-cfc23156-44ea-4500-bbbe-aa889650ccd0.png)

- Steve's parents' favorite stock DQ performed well in 2017 but also took a significant loss in 2018.

- Out of all stocks provided, "ENPH" and "RUN" stocks were the only stocks to have a net positive for both years.

- Refactoring reduced the run time to less than 10% of the original.

## Summary
- Refactoring code can greatly improve the efficiency of the subroutine.  However, with more variables and arrays in play, there is a greater chance of coding errors, requiring more extensive debugging.  Greater attention to detail is needed when assigning variables and arrays.

- The original AllStocksSummary subroutine was more readable and more easily understood.  Unfortunately, this resulted in a longer run time.

- The refactored AllStocksSummary subroutine had a shorter run time, but the code is less readable and had more difficult logic.

