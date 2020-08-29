from selenium import webdriver

# html content with selenium chromedriver
driver = webdriver.Chrome(executable_path = r'D:\Web Scraping\chromedriver_win32\chromedriver.exe')
driver.get('https://python.org')
html_doc = driver.page_source
print(html_doc)
driver.quit()