import requests, json
from bs4 import BeautifulSoup
import sys
import io
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://www.wishket.com/accounts/login/'

ua = UserAgent()

with requests.Session() as s:

    s.get(url)

    login = {
    'identification': 'magic95690',
    'password': 'hong4706',
    'csrfmiddlewaretoken': s.cookies['csrftoken']
    }

    response = s.post(url,data=login,headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        project = soup.select("table.table-responsive > tbody > tr")
        for i in project:
            pro = i.find('th').string
            num = i.find('td').text

            print('{} : {}'.format(pro,num))
