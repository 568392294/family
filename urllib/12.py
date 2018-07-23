from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml")
data = driver.title
print(data)
print(driver.page_source)