from selenium import webdriver
import time

driver = webdriver.Opera()
driver.get('https://www.youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')

searchbox.send_keys('mirage guild wars 2')

buisiness = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
buisiness.click()

time.sleep(5)

driver.save_screenshot('5.jpg')

time.sleep(15)
driver.quit()

