# School_District_Analysis

## Project overview
Maria, a data scientist for the school district, regularly compiles standardized math and reading scores and aggregates multiple datasets to help determine school performance on multiple levels, as well as how school funding may affect test scores.  Upon an internal audit, it was discovered that there may have been academic dishonesty and score manipulation within the 9th grade class at Thomas High School.  The school board is looking for an updated analysis, excluding the test scores from the 9th grade class at THS.

1. The Reading and Math scores from the THS 9th grade class should be removed from the dataset and the analysis.
2. The overall school district analysis should be recreated, excluding the data from the THS 9th grade class.

## Resources
- Data Sources: schools_complete.csv; students_complete.csv
- Software: Anaconda Prompt 4.13.0; Jupyter Notebook


## Results
Additional analysis of the data shows:

1. **District Summary:** There are slight drops in Average Math Score and Passing Percentages.  Average Reading Score was mostly unaffected.
![DSBefore](https://user-images.githubusercontent.com/106561880/177211282-1d842709-5fb9-4b00-86ff-a899a0cb318d.png)
![DSAfter](https://user-images.githubusercontent.com/106561880/177211293-f1895264-8b5e-43ad-82ff-ff444536cc05.png)

2. **School Summary:** Other schools are not affected, but Thomas High School shows drops in Average Math Score and Passing Percentages.  Average Reading Score went up slightly.
![PSSumBefore](https://user-images.githubusercontent.com/106561880/177211517-a5e3c012-8745-4afc-99a5-5c7b8effc51e.png)
![PSSumAfter](https://user-images.githubusercontent.com/106561880/177211529-4e44cfcb-67ba-43d5-af0c-e340fe81dc5e.png)

3. **Top Schools Ranking:** Overall rankings did not change, but again, THS shows drops in Average Math Score and Passing Percentages.  Again, Average Reading Score went up slightly.
![TopBefore](https://user-images.githubusercontent.com/106561880/177211359-cbe83ca0-6fb7-4c7a-8c41-61430694d062.png)
![TopAfter](https://user-images.githubusercontent.com/106561880/177211366-6ca62d10-c89a-457d-ac04-2a100667b2b2.png)

4. **Math and Reading Scores by Grade:** Other grades are not affected.  9th grade scores for THS were removed.
![MBGBefore](https://user-images.githubusercontent.com/106561880/177211401-d19e5f68-e2e0-449f-b2be-3ca43cb42c94.png)![MBGAfter](https://user-images.githubusercontent.com/106561880/177211407-48ebafb8-73a2-4606-8bb5-3720afe1f17a.png)

   ![RBGBefore](https://user-images.githubusercontent.com/106561880/177211422-2c209b83-b1c6-4749-a94a-c76ce31f6675.png)![RBGAfter](https://user-images.githubusercontent.com/106561880/177211433-91fc579d-81fb-49d6-9afb-86ef93574b61.png)

5. **Spending Ranges:** Spending Ranges per student are largely unaffected.
![SSumBefore](https://user-images.githubusercontent.com/106561880/177211335-5a1e7441-8620-4553-aa73-c2b1184a6585.png)
![SSumAfter](https://user-images.githubusercontent.com/106561880/177211341-4c71692e-ace9-46f6-85b5-99be3fde01f6.png)

6. **School Size:** Average Scores and Passing Percentages are largely unaffected.
![SSizeBefore](https://user-images.githubusercontent.com/106561880/177211548-aaf63f83-a723-4cac-93a2-b40084870fba.png)
![SSizeAfter](https://user-images.githubusercontent.com/106561880/177211555-ffd7638f-210b-43b0-aaa3-3eba5df16b5f.png)

7. **School Type:** Average Scores and Passing Percentages are largely unaffected.
![STypeBefore](https://user-images.githubusercontent.com/106561880/177211566-e08cc631-10af-456d-8db9-b9d46177275b.png)
![STypeAfter](https://user-images.githubusercontent.com/106561880/177211575-6fee7bed-96c4-41fb-8bbf-dea8381a9d48.png)

## Summary
Removing the scores from the 9th grade class at Thomas High School only marginally changed their scores and did not affect their overall ranking in the school district.  As noted, their Average Math Score, Passing Math percentage, Passing Reading percentage, and Overall percentage went down slightly.  Average Reading Scores were not affected in the overall district and actually improved at THS.  With this information, if there was academic dishonesty with the 9th grade class at THS, it is likely it resulted from isolated incidents from within the class and not systemic of the entire grade.
