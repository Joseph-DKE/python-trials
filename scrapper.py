import requests
from bs4 import BeautifulSoup
from selenium import webdriver
 
#page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
#soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
 
#links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
#first10 = links[:10] # Keep only the first 10 anchors
#for anchor in first10:
#    print(anchor.text) # Display the innerText of each anchor



driver = webdriver.Chrome()
driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup. Notice driver.page_source instead of page.content
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor












#links = soup.select("select option")