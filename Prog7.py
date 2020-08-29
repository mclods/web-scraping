from selenium import webdriver
from bs4 import BeautifulSoup

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'Your_Path')
driver.get('https://www.flipkart.com')
html_doc = driver.page_source

# using beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')

# search all <div> tags with id
a_ids = soup.find_all('div', {'id':'container'})
print(a_ids)

driver.quit()