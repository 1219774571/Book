# BeautifulSoup数据筛选

| 解析器 | 使用方法 | 优势 | 劣势 |
| :--:  | :----:  | :--:|:--: |
| Python标准库| BeautifulSoup(markup,"html.parser")| python内置标准库，执行速度中，容错强 | python2.7.3或3.32前的版本中文容错差|
| lxml HTML解析器| BeautifulSoup(markup,"lxml")| 速度快，容错强| 需安装c库|
| lxml XML解析器| BeautifulSoup(markup,"xml")| 速度快，唯一支持XML解析器|需安装C库|
|html5lib| BeautifulSoup(markup,"html5lib")|最好的容错，以游览器方式解析，生成html5格式文档| 速度慢，不依赖外来扩展|

## 基本使用

```python
from bs4 import BeautifulSoup

url = '''<html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapperoff autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn">百度一下</span><p>测试</p></form> </div> </div> <div id=u'''
soup = BeautifulSoup(url,'lxml')
print(soup.prettify())
print(soup.title.string)
```

## 标签选择器

### 选择元素

```python
#同上
print(soup.head)
```

### 获取名称

```python
print(soup.title.name)
```

### 获取属性

```python
print(soup.input.attrs['type'])
print(soup.input['type'])
```

### 获取内容

```python
print(soup.p.string)
```

### 嵌套选择

```python
print(soup.head.title.string)
```

### 子节点和子孙节点

```python
print(soup.p.contents)
#子节点soup.p.children
#子孙节点soup.p.descendants
for i, child in enumerate(soup.p.descendants):
    print(i, child)
```

### 父节点和祖先节点

```python
print(soup.p.parent)
print(list(enumerate(soup.p.parents)))
```

### 兄弟节点

```python
print(list(enumerate(soup.p.next_siblings)))
print(list(enumerate(soup.p.[revious_siblings)))
```

## 标准选择器

find_all(name, attrs, recursive, text, **kwargs)

> 返回所有匹配标签
> 可根据标签名、属性、内容查找文档
>
> name 标签名 name='标签名'
>
> attrs 属性名 = {'id':'ok'} 也可 id='ok'更方便 
> class_名需要下划线 class_='ko'
> text 匹配文本 text='测试'

find(name, attrs, recursive, text, **kwargs)

> 返回一个

find_parents() find_parent()
返回所有祖先节点    返回直接父节点

find_next_siblings() find_next_sibling()
返回后面所有兄弟节点    返回后面第一个兄弟节点

find_previous_siblings() find_previous_sibling()
返回前面所有兄弟节点    ....

find_all_next() find_next()
返回节点后所有符合条件的节点    ...

find_all_previous() find_previous()
返回节点后所有符合条件的节点    ...

## CSS选择器

select()直接传入CSS选择器即可完成选择
```python
print(soup.select('input'))
```
## 获取属性

```python
for inpu in soup.select('input'):
    print(inpu['id'])
    print(inpu.attrs['id'])
```

## 获取内容

```python
for i in soup.select('input'):
    print(i.get_text())
```
