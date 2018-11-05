# Urllib

```python
import urllib.request
```

## 内置的HTTP请求库

> urllib.request 请求模块
>
> urllib.error 异常处理模块
>
> urllib.parse url解析模块
>
> urllib.rebotparser robots.txt解析模块

### urlopen()

> 打开url
> urllib.request.urlopen()

### decode('utf-8')

> 指定编码格式

### 响应类型

> type()

### 状态码、响应头

> status
> getheaders()

## Request

```python
import urllib.request, parse

url = "http://httpbin.org/post"
dict = {
    'name' : 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
request = urllib.request.Request(url=url, data=data, method='POST')
request.add_header('User-Agent', 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
```
## Handler 代理

```python
import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:8888',
    'https':'https://127.0.0.1:8888'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read().decode('utf-8'))
#此处是另外的

opener.addheader=['User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36']
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.baidu.com/s?wd=ip')
print(response.read().decode('utf-8'))
```

## Cookie

```python
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + " = " + item.value)
```

## URL解析

### urlparse

```python
form urllib.parse import urlparse
```

### urlunparse

```python
form urllib.parse import urlunparse
```

### urljoin

```python
form urllib.parse import urljoin
```

### urlencode

```python
form urllib.parse import urlencode
```