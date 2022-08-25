# Movies-ETL
## Project Overview
Amazing Prime is sponsoring a hackathon for their streaming service.  They are looking to create a clean dataset of movies and user rankings to help predict popular movies.  The ultimate goal is to find lower budget movies that have not yet been purchased for streaming services and buy exclusive rights to those movies.  Over the past week, our team has been perfecting the code to Extract the different data sources, Transform them into usable data, and Load them into a SQL database.  The bulk of this process is performed using Python in Jupyter Notebook.

The Purpose of this project to:
1. Make sure the ETL processes are working correctly.
2. Combine all these processes into a single function that can be used with future datasets.

## Results

Four different deliverables were created in order to achieve the final result:

1. The consolidation of the week's work that includes code that will read the data files and create three separate DataFrames

    ### Wikipedia Movie Info Dataframe
    ![01a_wiki_movies_df](https://user-images.githubusercontent.com/106561880/182266406-ff482dae-cfd5-47a3-8b52-b8342e537b67.png)


    ### Kaggle Metadata DataFrame
    ![01b_kaggle_metadata](https://user-images.githubusercontent.com/106561880/182266429-e2fe1700-c432-4f6e-a2c9-eb705b43a685.png)

    ### MovieLens Ratings DataFrame
    ![01c_ratings](https://user-images.githubusercontent.com/106561880/182266453-0aa4d3e9-79e8-4506-9e73-c42cbe427a16.png)



2. Extraction and Transformation of Wikipedia so it can be merged with Kaggle Metadata.

    ### Confirmation of Wikipedia Movie Info Dataframe
    ![02a_wiki_movies_df_head](https://user-images.githubusercontent.com/106561880/182266469-8e1095cf-ee13-456d-962c-aa92ae342541.png)


    ### Column List of Wikipedia Movie Info Dataframe
    ![02b_wiki_movies_columns](https://user-images.githubusercontent.com/106561880/182266487-72329ddf-f289-4901-95c8-6c6043452e50.png)



3. Extraction and Transformation of Kaggle and MovieLens data and merging of all Dataframes.

    ### Movies With Ratings and Movies Dataframes
    ![03b_movies_with_ratings](https://user-images.githubusercontent.com/106561880/182266532-ee57bd16-a6fe-4c3f-88bf-bd81e7bd77d8.png)
    ![03c_movies_df](https://user-images.githubusercontent.com/106561880/182266545-9d462b55-aea3-446c-b4f0-f8975c282d44.png)


4. Final creation of movie database as a function to load as tables into SQL.

    ### Confirmation of Movie Table Load

    ![movies_query](https://user-images.githubusercontent.com/106561880/182266566-6dd80914-6226-4734-ab35-2378a1dc22ec.png)

    ### Confirmation of Ratings Table Load
    
    ![ratings_query](https://user-images.githubusercontent.com/106561880/182266579-49f1fe87-582d-42e8-adaa-ddc6b495b9c2.png)

    
*Note: Source files, excluding MovieLens Ratings data, are located in SourceData folder.  MovieLens Ratings file is too large to upload.
Additional Note: Final output images, including final SQL queries, are in Resources folder.*
