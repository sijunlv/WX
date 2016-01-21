# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from ssdb import SSDB
from ssdb.connection import BlockingConnectionPool
import json
import uuid
import time

class myssdb_hash(object):

    def __init__(self, table, host='localhost', port=8888, **kwargs):
        self.name = table
        pool = BlockingConnectionPool(host=host, port=port, **kwargs)
        self.__conn = SSDB(connection_pool=pool)

    # put a data
    def put(self, value, **kwargs):
        if isinstance(value, dict):
            key = value.get('_id', str(uuid.uuid1()))
        elif isinstance(value, basestring):
            try:
                tmp = json.loads(value)
                if isinstance(tmp, dict):
                    key = tmp.get('_id', str(uuid.uuid1()))
                else:
                    key = str(uuid.uuid1())
            except:
                key = str(uuid.uuid1())
        else:
            key = str(uuid.uuid1())
        status = self.__conn.hset(self.name, key, value if isinstance(value, basestring) else json.dumps(value))
        self.__conn.hincr('counter_' + self.name, time.strftime('%Y-%m-%d', time.localtime(float(time.time()))))
        return status

    # get a data
    def get(self, **kwargs):
        tmp = self.__conn.hscan(self.name, '', '', limit=1)
        if not tmp:
            return None
        try:
            self.__conn.hdel(self.name, tmp.keys()[0])
        except Exception as e:
            print str(e)
            return None
        return tmp.values()[0]

    # table size
    def size(self, *args, **kwargs):
        return self.__conn.hsize(self.name)

    def __list(self):
        start_key = ''
        for i in xrange(0, self.size(), 1000):
            tmp = self.__conn.hscan(self.name, start_key, '', limit=1000)
            start_key = tmp.keys()[-1]
            for value in tmp.values():
                yield value

    def get_values(self):
        return self.__list()


if __name__ == '__main__':
    hash_queue = myssdb_hash('test', host='web12', port=54321)
    # 插入数据，并使计数器自增（用于统计每日数据流量）
    print hash_queue.put({'_id': 'id1', 'name': 'LVV'})
    print hash_queue.put({'_id': 'id1', 'name': 'BBD'})
    print hash_queue.put({'_id': 'id2', 'company': u'成都数联铭品科技有限公司'})
    # 遍历Hash表
    for value in hash_queue.get_values():
        print value
