# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class zong_he_jing_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.cheng_shi_ming_cheng = None
        self.jing_dian_ming_cheng = None
        self.men_piao_lei_xing = None
        self.cheng_ren_jia_ge = None
        self.er_tong_jia_ge = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'城市名称': self.cheng_shi_ming_cheng,
            u'景点名称': self.jing_dian_ming_cheng,
            u'门票类型': self.men_piao_lei_xing,
            u'成人价格': self.cheng_ren_jia_ge,
            u'儿童价格': self.er_tong_jia_ge
        }