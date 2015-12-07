# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class wei_bo_yong_hu(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.wei_bo_ming_cheng = None
        self.guan_zhu_shu = None
        self.fen_si_shu = None
        self.wei_bo_shu = None
        self.di_zhi = None

    def makemap(self):
        return {
            u'微博名称': self.wei_bo_ming_cheng,
            u'关注数': self.guan_zhu_shu,
            u'粉丝数': self.fen_si_shu,
            u'微博数': self.wei_bo_shu,
            u'地址': self.di_zhi
        }