# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 工厂类，生产字段对象
class FieldFactory(object):

    def __init__(self, datasource, version=1, *args, **kwargs):
        self.__datasource = datasource
        self.__version = version


    # 反射，创建相应对象
    def create(self, type, *args, **kwargs):
        return getattr(__import__(type), type)(datasource=self.__datasource, version=self.__version, *args, **kwargs)
