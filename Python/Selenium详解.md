# Selenium详解

自动化测试工具，支持多种游览器，爬虫中主要用来解决JavaScript渲染问题

## 基本使用

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.baidu.com'
browser = webdriver.Chrome()
try:
    browser.get(url)
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')#向元素发送一些键值
    input.send_keys(Keys.ENTER)#回车
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
```

## 声明游览器对象

```python
from selenium import webdriver
browser = webdriver.Chrome()
                    .FireFox()
                    .Edge()
                    .PhantomJS()
                    .Safari()
```

## 访问页面

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()
```

## 查找元素

### 单个元素

常用
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
input_first = browser.find_element(By.ID,'q')
print(input_first)
browser.close()
```

### 多个元素

在element后面加个s
```python
lis = browser.find_elements_by_css_selector('.service-bd li')
```

## 元素交互操作

对获取的元素调用交互方法

```python
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')#输入文本
time.sleep(1)
input.clear()
input.send_keys('图书')
button = browser.find_element_by_class_name('btn-search')
button.click()
```

## 交互动作

将动作附加到动作链中串行执行

```python
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
```

## 执行JavaScript

```python
from selenium import webdriver
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("脚本执行")')
```

## 获取元素信息

### 获取属性

```python
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
```

### 获取文本值

```python
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
```

### 获取ID、位置、标签名、大小

```python
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
```

## Frame

```python
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source)
```

## 等待

### 隐式等待

使用隐式等待执行时，没有DOM中的元素，等待指定时间，超出则抛出异常，默认0

```python
from selenium import webdriver
# 一样打开谷歌
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
```

### 显式等待

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 同
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
```

## expected_conditions as EC 使用方法

- title_is: 判断当前页面的title是否精确等于预期
- title_contains: 判断当前页面的title是否包含预期字符串
- presence_of_element_located: 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
- visibility_of_element_located: 判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
- visibility_of: 跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
- presence_of_all_elements_located: 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
- text_to_be_present_in_element: 判断某个元素中的text是否包含了预期的字符串
- text_to_be_present_in_element_value: 判断某个元素中的value属性是否包含了预期的字符串
- frame_to_be_available_and_switch_to_it: 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
- invisibility_of_element_located: 判断某个元素中是否不存在于dom树或不可见
- element_to_be_clickable: 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
- staleness_of: 等某个元素从dom树中移除，注意，这个方法也是返回True或False
- element_to_be_selected: 判断某个元素是否被选中了,一般用在下拉列表
- element_selection_state_to_be: 判断某个元素的选中状态是否符合预期
- element_located_selection_state_to_be: 跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
- alert_is_present: 判断页面上是否存在alert，这是个老问题，很多同学会问到

## 前进后退

```python
import time
from selenium import webdriver

browser.back()#后退
time.sleep(1)
browser.forward()#前进
```

## Cookies

```python
from selenium import webdriver

#一样
browser.add_cookie({'name':'sb','domain':'知乎'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
```

## 选项卡

```python
import time
from selenium import webdriver

browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
```
