# -*- coding: utf-8 -*-
# @Time: 2022/11/24 20:27
# @Project: Reinforcement-Learning-YOLOv5-Project
# @Author: 唐天扬
# @Function: 获取直播真实URL，用于抓取流文件
import requests


class ZhiBotv:

    def __init__(self, rid):
        """
        抓取中国体育&新传宽频直播流，直播间地址示例如：https://v.zhibo.tv/10007
        Args:
            rid:体育直播房间号
        """
        self.rid = rid
        self.params = {
            'token': '',
            'roomId': self.rid,
            'angleId': '',
            'lineId': '',
            'definition': 'hd',
            'statistics': 'pc|web|1.0.0|0|0|0|local|5.0.1',
        }
        self.BASE_URL = 'https://rest.zhibo.tv/room/get-pull-stream-info-v430'
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.69 Safari/537.36 ',
            'Referer': 'https://www.zhibo.tv/live/'
        }

    def get_real_url(self):
        """
        no streaming 没开播;
        non-existent rid 房间号不存在;
        :return: url
        """
        with requests.Session() as s:
            res = s.get(self.BASE_URL, params=self.params, headers=self.HEADERS).json()
            if 'hlsHUrl' in res['data']:
                url = res['data'].get('hlsHUrl')
                if url:
                    return url
                else:
                    raise Exception('no streaming')
            else:
                raise Exception('non-existent rid')


def get_real_url(rid):
    try:
        zbtv = ZhiBotv(rid)
        return zbtv.get_real_url()
    except Exception as e:
        print('Exception：', e)
        return False


if __name__ == '__main__':
    r = input('请输入中国体育房间号：\n')
    print(get_real_url(r))