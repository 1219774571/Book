# 作者: coffee
# 时间: 2018年11月04日05:28:23
# 脚本: 爬取百度图片的爬虫
# 版本: V1.8

import getopt
import multiprocessing
import os
import signal
import sys
from json import JSONDecodeError
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from requests import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': '',
}
args = {}
default_path = os.getcwd() + '/images'
data = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': '201326592',
    'fp': 'result',
    'queryWord': '',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'st': '-1',
    'ic': '0',
    'word': '',
    'pn': 0,
    'rn': '30'
}
index_url = {
    'tn': 'baiduimage',
    'ct': '201326592',
    'lm': -1,
    'cl': 2,
    'ie': 'gb18030',
    'word': '',
    'fr': 'ala',
    'ala': 1,
    'alatpl': 'others',
    'pos': 0
}
img_url = {
    'ct': '503316480',
    'spn': 0,
    'ie': 'utf-8',
    'word': '',  # 搜索名
    'pn': 0,  # 图片数
    'di': '',  # json
    'cs': '',
    'os': ''
}
index = 'http://image.baidu.com/search/index?'
jsonUrl = 'http://image.baidu.com/search/acjson?'
imgUrl = 'http://image.baidu.com/search/detail?'


def src():
    data['queryWord'] = args['i']
    data['word'] = args['i']
    index_url['word'] = args['i']
    img_url['word'] = args['i']


def get_one_page():
    try:
        response = requests.get(jsonUrl, headers=headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            print('获取页面失败，状态:', response.status_code)
            return None
    except RequestException:
        print('请求异常')
        return None
    except JSONDecodeError:
        print('json解析失败')
        return None


def parse_one_page(html):
    img = []
    for i in html['data']:
        if 'di' in i:
            img_url['di'] = i['di']
        if 'cs' in i:
            img_url['cs'] = i['cs']
        if 'os' in i:
            img_url['os'] = i['os']
        img.append(imgUrl + urlencode(img_url) + '&tn=baiduimagedetail&gsm=0&rpstart=0&rpnum=0&islist=&querylist=')
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
        print("访问下载连接失败")
        return None
    if response.status_code == 200:
        save_image(response, url.split('/')[-1])
    else:
        print('文件无法下载，状态:', response.status_code)


def save_image(img, name):
    path = parse_path()
    path = '{0}/{1}'.format(path, name)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(img.content)
        print('图片', path, '下载完成')
    else:
        print('图片', path, '已存在,自动跳过')


def parse_args():
    show_args()
    get_args()
    if 'i' not in args.keys():
        print("图片名是必须的")
        sys.exit(1)
    if 'n' not in args.keys():
        args['n'] = 1
    if 'p' not in args.keys():
        args['p'] = multiprocessing.cpu_count()


def show_args():
    if len(sys.argv) < 2:
        print("-n 爬取次数 默认=1")
        print("-i 爬取图片名字")
        print("-o 输出目录，无则下载到当前目录images,无images则创建")
        print("-p 指定线程数，默认=cpu核数")
        sys.exit(0)


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


def parse_image_url(url):
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text, 'lxml')
    image_url = html.select('#hdFirstImgObj')
    if image_url:
        return image_url[0]['src']
    else:
        print('获取图片url失败,状态', response.status_code)
        return None


def main():
    response = get_one_page()
    if not response:
        return None
    url = parse_one_page(response)
    if not url:
        return None
    for image in url:
        image_url = parse_image_url(image)
        if image_url:
            download_img(image_url)


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def start():
    for offset in range(args['n']):
        print('第', offset + 1, '轮')
        data['pn'] = offset * 30
        img_url['pn'] = offset
        main()


if __name__ == '__main__':
    parse_args()
    src()
    requests.get(index, headers=headers, params=index_url)
    pool = multiprocessing.Pool(args['p'], init_worker)
    try:
        pool.apply_async(start())
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()
