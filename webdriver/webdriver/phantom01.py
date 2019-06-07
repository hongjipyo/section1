import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS('C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/webdriver/phantomjs/phantomjs.exe')

driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/결과물/website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/결과물/website2.png")

driver.quit()

print('완료')
