



import requests, json
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#로그인 유저정보
LOGIN_INFO = {
    'email':'9219560@naver.com',
    'password':'hong4706*'
}

#Session생성
with requests.Session() as s:

    login_req = s.post('https://www.inflearn.com/api/signin', data=LOGIN_INFO)
    #소스 확인
    #print('login_req',login_req.text)
    #헤더 확인
    #print('header',login_req.headers)


    if login_req.status_code == 200 and login_req.ok:
        dash_info = s.get('https://www.inflearn.com/users/174986/dashboard')

        dash_info.raise_for_status()

        soup = BeautifulSoup(dash_info.text,'html.parser')

        statistics = soup.select("div.box.statistics > div.box_content > div > div")

        for v in statistics:

            label = v.find('div', class_="status_label").text.strip()

            status = v.find('div', class_="status_value").text.strip()

            print('{} : {}'.format(label, status))
