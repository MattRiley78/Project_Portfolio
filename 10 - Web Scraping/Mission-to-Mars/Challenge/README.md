# Mission-to-Mars
## Project Overview
Robin is attempting to create a web app that will scrape data from various online sources to create a central location to compile all the data she is interested in.  After spending the week building and testing the code in Jupyter Notebook, transferring to Python files, and using Flask to transfer to the html file, she is wanting to add an additional set of hemispherical images to her app.

## Methods
- Splinter was imported to scrape data from various websites.
- BeautifulSoup was imported to help scrape data.
- ChromeDriverManager was imported to set up Splinter.
- Jupyter Notebook was used to test code.
- Code was entered into Python and modified using VSCode.
- Flask was imported to render html templates.
- MongoDB was used to store data.
- Bootstrap Style was added to html code to polish output.

## Problems and Solutions
Creating the code did present some problems requiring troubleshooting.  

- Jupyter Notebook code for the hemispherical images were not iterating correctly.  Iterator had to be added before .click() code to get to run correctly.
- Python code was returning no output for hemispherical images.  After troubleshooting, code kept returning Internal Server Errors.  Additional troubleshooting showed that the database had been corrupted.  Compass was installed.  Collection and database were dropped and reinitiated.

## Deliverable Images
Final Jupyter Notebook code to retrieve image urls and titles as a list of dictionaries.
![Deliverable_1](https://user-images.githubusercontent.com/106561880/185507575-636ed081-99b0-43fe-8b65-c7442d03fae2.png)

Hemispherical images scraped and added to HTML file.

![Deliverable_2](https://user-images.githubusercontent.com/106561880/185507583-5584b22a-bf36-499b-8cbe-c777f471ecc7.png)

## Additional Enhancements
Code was added to beautify the page, including:
- Body background image
- Background image in Jumbotron header, plus additional Jumbotron enhancements.
- Script activating button modified to blend into new Jumbotron background.
- Font colors changed to white to be readable over dark background image.
- Blockquote and text classes added to News Scrape to make it stand out.
- Additional code added to make content responsive to different screen sizes.
- Hemispherical images reduced in size using responsive code.  Images did not need to be that large on a large screen.
