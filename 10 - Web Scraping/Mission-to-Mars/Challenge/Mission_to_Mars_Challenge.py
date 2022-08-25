#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
#Import Pandas
import pandas as pd


# In[2]:


# Set your executable path.
# Sets up Splinter and opens browser.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Scrape the News

# In[3]:


# Visit the Mars NASA News Site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Set up HTML parser, converting browser html to a soup object.
html = browser.html
news_soup = soup(html, 'html.parser')
# First News Slide
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


#Call the slide element
slide_elem


# In[6]:


#Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Get the summary text
summary_text = slide_elem.find('div', class_='article_teaser_body').get_text()
summary_text


# ### Scrape the Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image URL
# After inspecting the image code
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create the full URL link
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Scrape an entire table (for Mars Facts)

# In[13]:


# Create Pandas DF that will read html.  Index 0 to only read first table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
# Name the DF columns
df.columns=['Description', 'Mars', 'Earth']
# Set the index and hold in place
df.set_index('Description', inplace=True)
df


# In[14]:


# Convert to html
df.to_html()


# ### DELIVERABLE 1: Scrape High-Res Images and Titles

# In[15]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[16]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for page in range(0, 4):
    hemispheres = {}

    thumblink = browser.find_by_tag("h3")[page] 
    thumblink.click()
    
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    img_url_rel = news_soup.find('a', href=True, text="Sample").get('href')
    img_url = f'https://marshemispheres.com/{img_url_rel}'
    title = browser.find_by_tag("h2").text
    hemispheres['img_url'] = img_url
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[17]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[18]:


# Close the browser
browser.quit()


# In[ ]:




