import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/webdriver/chrome/chromedriver.exe")

#driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/결과물/website5.png")

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/결과물/website6.png")

driver.quit()

print('완료')
