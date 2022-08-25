# UFOs
## Project Overview
Dana needs to create an HTML page using Javascript to pull in data from UFO sightings and display them in a table.  While learning the Javascript code, she was able to create one filter for date of each sighting.  This was implemented with a button.  The purpose of this project is to add to the code so that multiple filters can be applied based on user input. 

## Methods
Data is stored in a Javascript file, data.js.  An app.js file was created to import the data from data.js, and then implement functions to insert the table into an HTML file.  The index.html file was created with Bootstrap elements so that it will present the data neatly.

In the app.js file, the code was updated where instead of the user pressing a button to filter one type of data, two different functions were created.  One function stores the filtered data that was entered by the user.  The second function filters the table based on that input.  The listening event was also changed from a button click to any time there is a change to the input.

## Results

### Extra Filters Added and Button Removed.  Full Table Is Displayed.
![filteredtable](https://user-images.githubusercontent.com/106561880/185832416-f24cdb24-80cb-4b48-8150-5a647712b97e.png)


### Example of User Input and Filtered Table
![filteredtable2](https://user-images.githubusercontent.com/106561880/185832423-b125ee74-bdc6-4d54-bf1c-0cb217a0ffcf.png)




## Summary and Recommendations
While this webpage is functional, the dataset is relatively small.  The date range of the data set is only 2 weeks' worth in January of 2010.  Since the entire table is displayed upon page load, this could increase page load times if there is an extensive data file loaded.  Another drawback is that the user may not be aware of all the possible filters and may become disappointed if they search for cities that are not located on the dataset.

For future development of this website, I would recommend that instead of text entry fields, drop-down menus are implemented.  That way, a user can more easily search for criteria.  I would also recommend adding back the button that will implement ANY and ALL filters once they are selected by the user.  This way, if a user wants to filter by multiple criteria, they will only have to filter the output once.  Also, if the dataset becomes too large, it may be best to set the default output to none until filters are selected.
