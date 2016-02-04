# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from ssdb import SSDB
from ssdb.connection import BlockingConnectionPool
import json
import time


class myssdb(object):

    def __init__(self, table=None, host='localhost', port=8888, **kwargs):
        self.table = table
        pool = BlockingConnectionPool(host=host, port=port, **kwargs)
        self.ssdb = SSDB(connection_pool=pool)


    # 队尾放入一条数据
    def put(self, data, **kwargs):
        length = 0
        if isinstance(data, dict) or isinstance(data, list):
            length = self.ssdb.qpush_back(self.table, json.dumps(data))
        else:
            length = self.ssdb.qpush_back(self.table, data)
        if length:
            self.ssdb.hincr('counter_' + self.table, time.strftime('%Y-%m-%d', time.localtime(float(time.time()))))
        return length


    # 队首取出一条数据
    def get(self, **kwargs):
        data = self.ssdb.qpop_front(self.table)
        if data:
            return data[0]
        return data


if __name__ == '__main__':
    ssdb = myssdb('test_queue', host='web12', port=54321)
    print ssdb.put({'name': 'lvv'})