import sys
import io
import requests, json


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

payload1 = {'key1':'value1', 'key2':'value2'}
payload2 = (('key1','value1'),('key2','value2'))
payload3 = {'some':'nice'}

#r = requests.put('http://httpbin.org/put', data=payload1)
#r.raise_for_status()
#print(r.text)

#r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
#print(r.text)

r= requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
