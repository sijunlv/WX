# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_ji_huo_che_piao(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.che_piao_ming = None
        self.chu_piao_fei = None
        self.shi_yong_tian_shu = None
        self.zuo_wei_lei_xing = None
        self.che_piao_lei_xing = None
        self.cheng_ren = None
        self.er_tong = None
        self.qing_nian = None
        self.zhang_zhe = None

    def makemap(self):
        return {
            u'车票名': self.che_piao_ming,
            u'出票费': self.chu_piao_fei,
            u'使用天数': self.shi_yong_tian_shu,
            u'座位类型': self.zuo_wei_lei_xing,
            u'车票类型': self.che_piao_lei_xing,
            u'成人': self.cheng_ren,
            u'儿童': self.er_tong,
            u'青年': self.qing_nian,
            u'长者': self.zhang_zhe
        }