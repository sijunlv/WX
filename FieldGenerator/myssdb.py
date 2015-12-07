# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from ssdb import SSDB
from ssdb.connection import BlockingConnectionPool
import json


class myssdb(object):

    def __init__(self, table=None, host='localhost', port=8888, **kwargs):
        self.table = table
        pool = BlockingConnectionPool(host=host, port=port, **kwargs)
        self.ssdb = SSDB(connection_pool=pool)


    # 队尾放入一条数据
    def put(self, data, **kwargs):
        if isinstance(data, dict) or isinstance(data, list):
            self.ssdb.qpush_back(self.table, json.dumps(data))
        else:
            self.ssdb.qpush_back(self.table, data)


    # 队首取出一条数据
    def get(self, **kwargs):
        data = self.ssdb.qpop_front(self.table)
        if data:
            return data[0]
        return data