# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from ssdb import SSDB
from ssdb.connection import BlockingConnectionPool
import json
import uuid


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
        return self.__conn.hset(self.name, key, value if isinstance(value, basestring) else json.dumps(value))

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


if __name__ == '__main__':
    hash_queue = myssdb_hash('test', host='web12', port=54321)
    print hash_queue.size()
    # _id is key!!!
    data1 = {'_id': '123', 'name': 'LVV'}
    data2 = {'_id': '123', 'name': 'BBD'}
    hash_queue.put(data1)
    print hash_queue.size()
    hash_queue.put(data2)
    print hash_queue.size()
    print hash_queue.get()
    print hash_queue.size()
    print hash_queue.get()
    print hash_queue.size()