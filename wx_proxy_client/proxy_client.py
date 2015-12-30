# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append('../')
sys.path.append('gen-py')

from jproxy import JProxy

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class ProxyClient(object):

    def __init__(self, host='spider8', port=6660, area=u'中国'):
        self.area = area if isinstance(area, str) else area.encode('utf-8')
        try:
            self.transport = TTransport.TBufferedTransport(TSocket.TSocket(host, port))
            self.client = JProxy.Client(TBinaryProtocol.TBinaryProtocol(self.transport))
            self.transport.open()
        except Thrift.TException, ex:
            print '%s' % (ex.message)

    def __del__(self):
        self.transport.close()

    def get(self):
        return self.client.get(self.area)