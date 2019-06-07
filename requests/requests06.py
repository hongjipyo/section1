import sys
import io
from bs4 import BeautifulSoup
import requests, json


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'user_id':'magic95690',
    'user_pw':'HONG4706'
}

#Session생성
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    #소스 확인
    #print('login_req',login_req.text)
    #헤더 확인
    #print('header',login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4661724&find=&ftext=')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text,'html.parser')
        #print(soup.prettify())
        article = soup.select_one("table:nth-child(1)").find_all('p')
        for i in article:
            if i.string is not None:
                print(i.string)
