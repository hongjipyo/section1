import sys
import io
import requests, json


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r= requests.put('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=5011025900')
print(r.text)
