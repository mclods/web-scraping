from selenium import webdriver
from bs4 import BeautifulSoup

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'D:\Web Scraping\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://www.techgig.com')
html_doc = driver.page_source

# using beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')

# search for all child
# div_tag = soup.find('div', class_ = 'right-column')
# all_div_children = div_tag.findChildren()
# print(all_div_children)

# search for direct parent
# div_tag = soup.find('div', class_ = 'right-column')
# div_parent = div_tag.findParent()
# print(div_parent)

# search for siblings
first_div = soup.find('div')
remaining_siblings = first_div.findNextSiblings()
print(remaining_siblings)

driver.quit()