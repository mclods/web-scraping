from selenium import webdriver
from bs4 import BeautifulSoup

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'Your_Path')
driver.get('https://python.org')
html_doc = driver.page_source

# using beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')

# search for all the <a> tags by name
a_tags = soup.find_all('a')
print(a_tags)
print("Length of the List = "+str(len(a_tags)))

driver.quit()