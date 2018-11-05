# Request

```python
import requests
requests.get('http://')
```

## 各种请求方式

```python
import requests
requests.post('http://')
requests.put('http://')
requests.delete('http://')
requests.head('http://')
requests.options('http://')
```

## 添加headers

```python
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.get("https://www.zhihu.com", headers=headers, verify=False)
print(response.text)
```

## 会话维持

```python
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456')
response = s.get('http://httpbin.org/cookies')
print(response.text)
```

## 证书验证

```python
import requests
response = requests.get('https://www.12306.cn')
print(response.status_code)

#消除警报信息
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://ip.cn', verify=False)
print(response.status_code)

response = requests.get('https://www.12306.cn',cert=('/path/server.crt', '/path/key'))
print(response.status_code)
```

## 代理设置

```python
import requests
proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "socks5://127.0.0.1:1080"
}
response = requests.get("https://ip.cn",proxies=proxies)
print(response.status_code)
```

## 超时设置

```python
import requests
from requests.exceptions import ReadTimeout
try:
    response = requests.get("http://ip.cn",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("Timeout")
    response = requests.get("http://ip.cn",timeout=1)
    print(response.status_code)
```

## 认证设置

```python
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://127.0.0.1',auth=('user','123'))
print(r.status_code)
```