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
    #index = 'http://image.baidu.com/search/index?' + urlencode(index_url)
    try:
        #requests.get(index, headers=headers)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except RequestException:
        print('请求出现异常', response.status_code)
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
        if not os.path.isdir(os.getcwd() + '/images'):
            os.mkdir(os.getcwd() + '/images', 0o755)
        return os.getcwd() + '/images'
    else:
        if not os.path.isdir(args['o']):
            try:
                os.mkdir(args['o'], 0o755)
            except FileNotFoundError:
                os.makedirs(args['o'], 0o755)
        return args['o']


def download_img(url):
    try:
        response = requests.get(url, stream=True, headers=headers)
    except RequestException:
        print("下载错误", response.status_code)
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
            f.close()
            print('图片', url, '下载完成')
    else:
        print(path, '图片已存在, 自动跳过')


def main(offset):
    url = get_url_page(offset)
    print("解析url为", url)
    response = get_one_page(url)
    url = parse_one_page(response)
    if not url:
        return
    print('解析完成,开始下载')
    for image in url:
        if image:
            download_img(image)
    print('当前页面下载结束')


def parse_args():
    show_args()
    get_args()
    if 'i' not in args.keys():
        print("图片名是必须的")
        sys.exit(1)
    try:
        if not args['p'].isdigit() or not args['n'].isdigit():
            print('指定值必须是数字,当前-p为:', args['p'], '-n为', args['n'])
            sys.exit(1)
    except KeyError:
        pass
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
    opts, arg = getopt.getopt(sys.argv[1:], "n:i:o:p:")
    for option in opts:
        if option[0] == '-n':
            args['n'] = option[1]
        elif option[0] == '-i':
            args['i'] = option[1]
        elif option[0] == '-o':
            args['o'] = option[1]
        elif option[0] == '-p':
            args['p'] = option[1]
        else:
            print('异常竟然没处理，看来get_args方法出现问题了')
            sys.exit(1)


if __name__ == '__main__':
    parse_args()
    try:
            s = [30*i for i in range(int(args['n']))]
    except ValueError:
        print('-n 指定数值错误')
        sys.exit(2)
    pool = Pool(processes=int(args['p']))
    if 'o' in args.keys():
        pool.map(main, s)
    else:
        pool.map(main, s)
