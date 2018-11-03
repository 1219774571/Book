# 作者: coffee
# 时间: 2018年11月04日05:28:23
# 脚本: 爬取百度图片的爬虫
# 版本: V1.1

import getopt
import hashlib
import os
import re
import sys
from multiprocessing.pool import Pool
from urllib.parse import urlencode
import requests
from requests import RequestException


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': ''
    }
args = {}


def get_url_page(num):
    name = args['i']
    data = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'fp': 'result',
        'queryWord': name,
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'st': '-1',
        'ic': '0',
        'word': name,
        'pn': num,
        'rn': '30'
    }
    return 'http://image.baidu.com/search/acjson?' + urlencode(data)


def get_one_page(url):
    name = args['i']
    index_url = {
        'tn': 'baiduimage',
        'ct': '201326592',
        'lm': -1,
        'cl': 2,
        'ie': 'gb18030',
        'word': name,
        'fr': 'ala',
        'ala': 1,
        'alatpl': 'others',
        'pos': 0
    }
    index = 'http://image.baidu.com/search/index?' + urlencode(index_url)
    try:
        requests.get(index, headers=headers)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except RequestException:
        print('请求出现异常', response.status_code)
        return
    return


def parse_one_page(html):
    img = []
    for i in html['data']:
        if 'hoverURL' in i:
            if re.match('http(.*?)jpg', i['hoverURL'], re.S):
                img.append(i['hoverURL'])
    return img


def download_img(url):
    try:
        response = requests.get(url, stream=True, headers=headers)
    except RequestException:
        print("下载错误", response.status_code)
        return
    if response.status_code == 200:
        save_image(response.content, url)


def parse_path():
    if 'o' not in args.keys():
        if not os.path.isdir(os.getcwd() + '/images'):
            os.mkdir(os.getcwd() + '/images', 0o755)
        return os.getcwd() + '/images'
    else:
        return args['o']


def save_image(img, url):
    path = parse_path()
    path = '{0}/{1}.{2}'. format(path, hashlib.md5(url.encode('utf-8')).hexdigest(), 'jpg')
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(img)
            f.close()
            print('此图片', url, '下载完成')


def main(offset):
    url = get_url_page(offset)
    print("解析url为", url)
    response = get_one_page(url)
    url = parse_one_page(response)
    for image in url:
        if image:
            download_img(image)


def parse_args():
    if len(sys.argv) < 2:
        print("-n number")
        print("-i 爬取图片名字")
        print("-o 输出目录，无则下载到当前目录images")
        sys.exit(2)
    opts, arg = getopt.getopt(sys.argv[1:], "n:i:o:")
    for option in opts:
        if option[0] == '-n':
            args['n'] = option[1]
        elif option[0] == '-i':
            args['i'] = option[1]
        elif option[0] == '-o':
            args['o'] = option[1]
        else:
            print("错误参数", option[0])
    if 'n' not in args.keys() or 'i' not in args.keys():
        print("数值和图片名是必须的")
        sys.exit(3)


if __name__ == '__main__':
    parse_args()
    s = [30*i for i in range(int(args['n']))]
    pool = Pool()
    if 'o' in args.keys():
        pool.map(main, s)
    else:
        pool.map(main, s)
