#!/usr/bin/python
# -*- coding: UTF-8 -*-



import re
import time

from NexusPHP.config import generateConfig
from NexusPHP.utility.function import now


def signIn(session, url):
    # 完整签到url
    if url == "https://pt.btschool.club/":
        attendanceUrl = 'https://pt.btschool.club/index.php?action=addbonus'
        with session.get(attendanceUrl) as res:
            r = re.compile(r'签到您获得\d+')
    else:
        attendanceUrl = url + '/attendance.php'
        with session.get(attendanceUrl) as res:
            r = re.compile(r'签到已得\d+')

        # attendanceUrl = url + '/attendance.php'

        tip = r.search(res.text).group() if r.search(res.text) else res.text
        print(now(), '网站：%s' % (url), tip, '魔力值')


def main():
    print(now(), '签到开始：')
    [signIn(config['session'], config['url']) for config in generateConfig() if 'sign_in' in config['tasks']]

if __name__ == '__main__':
    main()
