# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class wei_bo_re_sou_bang(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.pai_ming = None
        self.guan_jian_ci = None
        self.sou_suo_ci_shu = None

    def makemap(self):
        return {
            u'排名': self.pai_ming,
            u'关键词': self.guan_jian_ci,
            u'搜索次数': self.sou_suo_ci_shu
        }