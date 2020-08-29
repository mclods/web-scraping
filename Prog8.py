from selenium import webdriver
from bs4 import BeautifulSoup

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'D:\Web Scraping\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://kiit.ac.in')
html_doc = driver.page_source

# using beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')

# search all tags with string
all_strings = soup.find_all('a', string = 'Skip to content')
print(all_strings)

driver.quit()