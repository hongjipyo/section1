import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome('C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/webdriver/chrome/chromedriver.exe')
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/api/signin')
time.sleep(5)
driver.implicitly_wait(3)

driver.find_element_by_name('')
