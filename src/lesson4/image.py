# -*- coding: utf-8 -*-
# Created by zed
import requests
import os
import sys

root = sys.path[0]
key = 'e3d33afd0211d9d5ad5ddc9241ef8189'
apis = {
    'meinv': 'http://api.tianapi.com/meinv/'
}


def save_image(name, url):
    path = root + '/images'
    if not os.path.exists(path):
        os.mkdir(path)
    image_path = path + '/' + name + '.' + url.split('.')[-1]
    f = open(image_path, 'wb+')
    f.write(get(url).content)
    f.close()
    print(image_path + '已保存')


def meinv_list(page, size=15):
    # print({'page': page, 'num': size})
    return get(apis['meinv'], {'page': page, 'num': size}).json()


def get(url, params=None):
    if params is None:
        params = {}
    params['key'] = key
    return requests.get(url, params)


def get_page():
    try:
        pages = int(input('获取几页数据？(ctrl+c 退出)\n'))
    except ValueError:
        print('非法的页数\n')
        return False
    return pages

def get_size():
    size = input('每页数据条数[默认15条]？(ctrl+c 退出)\n')
    if not size:
        return 15
    else:
        try:
            return int(size)
        except ValueError:
            print('非法的每页条数')
            return False


def main():
    while True:
        pages = get_page()
        if not pages:
            continue

        size = get_size()
        if not size:
            continue

        for page in range(1, pages+1):
            response = meinv_list(page, size)

            for item in response['newslist']:
                save_image(item['title'], item['picUrl'])



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('bye bye~')
        exit()
