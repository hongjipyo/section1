import sys
import io
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWrite:
    #초기화
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/magic/Desktop/코딩 공부/python 크롤링/section3/webdriver/chrome/chromedriver.exe")
        self.driver.implicitly_wait(5)

    def writecheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('9569magic')
        self.driver.find_element_by_name('pw').send_keys('hong4706*')
        self.driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr/td/table/tbody/tr[3]/td/input').click()
        self.driver.get('')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')



    #소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포ㅓ스된 영역 종료
        self.driver.quit() #전체 프로그램 종표
        print("Remove")

if __name__ == '__main__':
    a = NcafeWrite()

    start_time = time.time()
    a.writecheck()
    print("---Total %s secounds ---" % (time.time() - start_time))
    del a
