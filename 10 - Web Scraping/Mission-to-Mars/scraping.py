#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
#Import Pandas
import pandas as pd
import datetime as dt

def scrape_all():
    # Set your executable path.
    # Sets up Splinter and opens browser.
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    #Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # stop webdriver and return data
    browser.quit()
    return data


### Scrape the News
def mars_news(browser):

    # Visit the Mars NASA News Site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up HTML parser.
    html = browser.html
    news_soup = soup(html, 'html.parser')
    # Add try/except for error handling
    try:
        # First News Slide
        slide_elem = news_soup.select_one('div.list_text')
        slide_elem.find('div', class_='content_title')

        #Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Get the summary text
        summary_text = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    return news_title, summary_text

### Featured Images

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image URL
        # After inspecting the image code
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url



### Scrape Mars Facts

def mars_facts():
    try: 
        # Create Pandas DF that will read html.  Index 0 to only read first table
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None

    # Name the DF columns
    df.columns=['Description', 'Mars', 'Earth']
    # Set the index and hold in place
    df.set_index('Description', inplace=True)

    # Convert to html
    return df.to_html()

if __name__ == "__main__":

    # If running as ascript, print scraped data
    print(scrape_all())
