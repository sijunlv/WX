# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class you_ji(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.di_qu = None
        self.cheng_shi = None
        self.you_ji_shu_liang = None

    def makemap(self):
        return {
            u'地区': self.di_qu,
            u'城市': self.cheng_shi,
            u'游记数量': self.you_ji_shu_liang
        }