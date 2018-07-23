from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


# 处理重定向，可以定时检查页面的某元素
# 如果和先前的不一致则可认为客户端重定向
def wait_for_load(driver):
    #elem = driver.find_element_by_tag_name("html")
    title = driver.find_element_by_tag_name("title")
    #print(title)
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)

        newtitle = driver.find_element_by_tag_name("title")
        if newtitle != title:
            return
        #try:
        #    elem = driver.find_element_by_tag_name("html")
        #except StaleElementReferenceException:
        #    return

driver = webdriver.PhantomJS(executable_path='./phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
wait_for_load(driver)
print(driver.page_source)
