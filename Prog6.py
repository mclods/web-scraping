from selenium import webdriver
from bs4 import BeautifulSoup

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'Your_Path')
driver.get('https://www.edx.org')
html_doc = driver.page_source

# using beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')

# search for first <p> tag with a class name
p_tag = soup.find('p', class_ = 'copyright')
print(p_tag)

# search for all <p> tags with a class name
p_tags = soup.find_all('p', class_ = 'copyright')
print(p_tags)

driver.quit()