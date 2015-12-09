# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class da_qi_api_shi_shi_ren_shu_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.zi_yuan_bian_ma = None
        self.ming_cheng = None
        self.shi_shi_ren_shu = None
        self.zui_da_jie_dai_ren_shu = None
        self.shi_jian = None
        self.shu_ju_lai_yuan = None

    def makemap(self):
        return {
            u'资源编码': self.zi_yuan_bian_ma,
            u'名称': self.ming_cheng,
            u'实时人数': self.shi_shi_ren_shu,
            u'最大接待人数': self.zui_da_jie_dai_ren_shu,
            u'时间': self.shi_jian,
            u'数据来源': self.shu_ju_lai_yuan
        }