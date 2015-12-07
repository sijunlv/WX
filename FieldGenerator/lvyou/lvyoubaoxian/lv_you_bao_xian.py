# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class lv_you_bao_xian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.bao_xian_lei_xing = None
        self.bao_xian_gong_si = None
        self.xiao_liang = None
        self.biao_qian = None
        self.bao_xian_ming_cheng = None
        self.bao_xian_qi_xian = None
        self.jia_ge = None

    def makemap(self):
        return {
            u'保险类型': self.bao_xian_lei_xing,
            u'保险公司': self.bao_xian_gong_si,
            u'销量': self.xiao_liang,
            u'标签': self.biao_qian,
            u'保险名称': self.bao_xian_ming_cheng,
            u'保险期限': self.bao_xian_qi_xian,
            u'价格': self.jia_ge
        }