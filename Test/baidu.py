# 作者: coffee
# 时间: 2018年11月04日05:28:23
# 脚本: 爬取百度图片的爬虫
# 版本: V1.2

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
default_path = os.getcwd() + '/images'


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
        print('请求出现异常')
        return
    return


def parse_one_page(html):
    img = []
    try:
        for i in html['data']:
            if 'hoverURL' in i:
                if re.match('http(.*?)jpg|png', i['middleURL'], re.S):
                    img.append(i['middleURL'])
    except TypeError:
        print('此处无源，换线重来')
        return
    return img


def parse_path():
    if 'o' not in args.keys():
        if not os.path.isdir(default_path):
            print('创建文件夹路径为', default_path)
            os.mkdir(default_path, 0o755)
        return default_path
    else:
        if not os.path.isdir(args['o']):
            try:
                print('创建指定文件夹路径为', args['o'])
                os.mkdir(args['o'], 0o755)
            except FileNotFoundError:
                os.makedirs(args['o'], 0o755)
        return args['o']


def download_img(url):
    try:
        response = requests.get(url, stream=True, headers=headers)
    except RequestException:
        print("下载错误")
        return
    if response.status_code == 200:
        save_image(response.content, url)
    else:
        print('文件无法下载，状态:', response.status_code)


def save_image(img, url):
    path = parse_path()
    path = '{0}/{1}.{2}'. format(path, hashlib.md5(url.encode('utf-8')).hexdigest(), 'jpg')
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(img)
            print('图片', path, '下载完成')
    else:
        print('图片', path, '已存在, 自动跳过')


def parse_args():
    show_args()
    get_args()
    if 'i' not in args.keys():
        print("图片名是必须的")
        sys.exit(1)
    if 'n' not in args.keys():
        args['n'] = 1
    if 'p' not in args.keys():
        args['p'] = 4


def show_args():
    if len(sys.argv) < 2:
        print("-n 爬取次数 默认=1")
        print("-i 爬取图片名字")
        print("-o 输出目录，无则下载到当前目录images,无images则创建")
        print("-p 指定进程数，默认=4")
        sys.exit(1)


def get_args():
    try:
        opts, arg = getopt.getopt(sys.argv[1:], "n:i:o:p:")
    except getopt.GetoptError:
        print('参数错误')
        sys.exit(1)
    for option in opts:
        try:
            if option[0] == '-n':
                args['n'] = int(option[1])
            elif option[0] == '-p':
                args['p'] = int(option[1])
            elif option[0] == '-i':
                args['i'] = option[1]
            elif option[0] == '-o':
                args['o'] = option[1]
            else:
                print('异常竟然没处理，看来get_args方法出现问题了')
                sys.exit(1)
        except ValueError:
            print('数值选项输入为错误')
            sys.exit(1)


def main(offset):
    url = get_url_page(offset)
    response = get_one_page(url)
    url = parse_one_page(response)
    if not url:
        return
    for image in url:
        if image:
            download_img(image)


if __name__ == '__main__':
    parse_args()
    s = [30*i for i in range(args['n'])]
    pool = Pool(processes=args['p'])
    pool.map(main, s)
