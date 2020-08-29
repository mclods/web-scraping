from selenium import webdriver
from bs4 import BeautifulSoup

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'D:\Web Scraping\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://python.org')
html_doc = driver.page_source

# using beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')

# search for first <p> tag by name
first_p_tag = soup.find('p')
print(first_p_tag)

driver.quit()