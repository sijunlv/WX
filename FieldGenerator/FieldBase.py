# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from abc import abstractmethod
import time
import uuid
import json


# 字段生成器基类
class FieldBase(object):

    def __init__(self, datasource, version):
        # 公共变量

        # 主键
        self.id = None
        # uuid
        self.uuid = None
        # 数据源
        self.__datasource = datasource
        # 版本号
        self.__version = version
        # 原始数据
        self.rawdata = None
        # 网页链接地址
        self.url = None
        # 保留字段1
        self.retain1 = None
        # 保留字段2
        self.retain2 = None


    # 字段映射表，需要派生类去实现，返回一个字典
    @abstractmethod
    def makemap(self):
        pass


    # 生成数据表，成功返回一个字典，失败返回None
    def make(self):
        if not self.id:
            print 'The _id is null'
            return None
        try:
            self.uuid = str(uuid.uuid1())
            publicdata = {
                '_id': self.id + '|_|' + self.__datasource,
                'uuid': self.uuid,
                'datasource': self.__datasource,
                'version': self.__version,
                'rawdata': self.rawdata,
                'url': self.url,
                'retain1': self.retain1,
                'retain2': self.retain2,
                'uptime': int(time.time()),
                'do_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(time.time())))
            }
            privatedata = self.makemap()
            if isinstance(privatedata, dict):
                for key in publicdata.keys():
                    if isinstance(publicdata[key], dict) or isinstance(publicdata[key], list):
                        publicdata[key] = json.dumps(publicdata[key])
                for key in privatedata.keys():
                    if isinstance(privatedata[key], dict) or isinstance(privatedata[key], list):
                        privatedata[key] = json.dumps(privatedata[key])
                return dict(publicdata, **privatedata)
            else:
                print 'The result is not dictionary'
                return None
        except Exception as e:
            print 'Exception: ' + str(e)
            return None