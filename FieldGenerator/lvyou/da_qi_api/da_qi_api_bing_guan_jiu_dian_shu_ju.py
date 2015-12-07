# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class da_qi_api_bing_guan_jiu_dian_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.zi_yuan_bian_ma = None
        self.ming_cheng = None
        self.deng_ji = None
        self.jing_du = None
        self.wei_du = None
        self.lian_xi_ren = None
        self.dian_hua = None
        self.ren_shu = None
        self.ting_che_shu = None
        self.fang_jian_shu = None
        self.di_zhi = None
        self.ying_ji_lian_xi_ren = None
        self.ying_ji_dian_hua = None
        self.di_qu_bian_ma = None

    def makemap(self):
        return {
            u'资源编码': self.zi_yuan_bian_ma,
            u'名称': self.ming_cheng,
            u'等级': self.deng_ji,
            u'经度': self.jing_du,
            u'纬度': self.wei_du,
            u'联系人': self.lian_xi_ren,
            u'电话': self.dian_hua,
            u'人数': self.ren_shu,
            u'停车数': self.ting_che_shu,
            u'房间数': self.fang_jian_shu,
            u'地址': self.di_zhi,
            u'应急联系人': self.ying_ji_lian_xi_ren,
            u'应急电话': self.ying_ji_dian_hua,
            u'地区编码': self.di_qu_bian_ma
        }