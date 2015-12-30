# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from proxy_client import ProxyClient

if __name__ == '__main__':
    proxy_client = ProxyClient()
    proxy = proxy_client.get()
    print proxy