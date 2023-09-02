# -*- coding: utf-8 -*-
# @Time: 2022/11/24 21:11
# @Project: Reinforcement-Learning-YOLOv5-Project
# @Author: 唐天扬
# @Function: 下载直播流文件
import requests
def download_video(url, referer, name, p_dir):
    headers = {
        'origin': 'https://v.zhibo.tv',
        'referer': 'https://www.zhibo.tv/live/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.69 Safari/537.36'
    }
    headers['referer'] = referer

    r = requests.get(url, stream=True, headers=headers) # 这里是下载

    length = float(r.headers['content-length'])
    f = open(p_dir + '\' + '{}.{}'.format(name, 'flv'), 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    print(url)
    print('开始下载{}'.format(url))
    for chunk in r.iter_content(chunk_size=10240):# 这里开始是进行分块保存，并计时
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + '{:.2f}'.format(p) + '%' + ' Speed: ' + '{:.2f}'.format(speed) + 'M/S')
                time1 = time.time()
        else:
            print('{}保存失败！'.format(name))
    f.close()
    print("{0}.{1}保存成功！".format(name, 'flv'))