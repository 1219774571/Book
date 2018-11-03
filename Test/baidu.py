import getopt
import hashlib
import os
import sys
from urllib.parse import urlencode
import requests
from requests import RequestException


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': ''
    }


def get_url_page(num, name):
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


def get_one_page(url, name):
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
            #if re.match('http(.*?)jpg', i['hoverURL'], re.S):
            img.append(i['hoverURL'])
    return img


def download_img(url, path):
    try:
        response = requests.get(url, stream=True, headers=headers)
    except RequestException:
        print("下载错误", response.status_code)
        return
    if response.status_code == 200:
        save_image(response.content, url, path)


def save_image(img, url, path):
    if not os.path.isdir(os.getcwd() + '/images'):
        if path == os.getcwd() + '/images':
            os.mkdir(path, 0o755)
    path = '{0}/{1}.{2}'. format(path, hashlib.md5(url.encode('utf-8')).hexdigest(), 'jpg')
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(img)
            f.close()


def main(offset, name, path=os.getcwd()+"/images"):
    url = get_url_page(offset, name)
    print("解析url为", url)
    response = get_one_page(url, name)
    url = parse_one_page(response)
    print("获取成功，进入下载")
    for image in url:
        if image:
            print(image)
            download_img(image, path)


def parse_args():
    opts, arg = getopt.getopt(sys.argv[1:], "n:i:o:")
    args = {}
    for option in opts:
        if option[0] == '-n':
            args['n'] = option[1]
        elif option[0] == '-i':
            args['i'] = option[1]
        elif option[0] == '-o':
            args['o'] = option[1]
        else:
            print("错误参数", option[0])
    return args


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("-n number")
        print("-i 爬取图片名字")
        print("-o 输出目录，无则下载到当前目录images")
        sys.exit(2)
    args = parse_args()
    if 'n' not in args.keys() or 'i' not in args.keys():
        print("数值和图片名是必须的")
        sys.exit(3)

    s = [30*i for i in range(int(args['n']))]
    for num in s:
        print("当前第%d轮" % int(num / 30))
        if 'o' in args.keys():
            main(num, args['i'], args['o'])
        else:
            main(num, args['i'])

