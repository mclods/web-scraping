from selenium import webdriver

# html content with selenium phantomjs driver in headless mode
driver = webdriver.PhantomJS(executable_path = r'Your_Path')
driver.get('https://python.org')
html_doc = driver.page_source
print(html_doc)
driver.quit()
