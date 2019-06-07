import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/webdriver/firefox/geckodriver.exe")

#driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/결과물/website7.png")

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/결과물/website8.png")

driver.quit()

print('완료')
