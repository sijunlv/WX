# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class zong_he_jing_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.cheng_shi_ming_cheng = None
        self.qu_guo_ren_shu = None
        self.dian_ping_tiao_shu = None
        self.jing_dian_pai_ming = None
        self.zong_he_ping_fen = None
        self.jing_dian_ming_cheng = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'城市名称': self.cheng_shi_ming_cheng,
            u'去过人数': self.qu_guo_ren_shu,
            u'点评条数': self.dian_ping_tiao_shu,
            u'景点排名': self.jing_dian_pai_ming,
            u'综合评分': self.zong_he_ping_fen,
            u'景点名称': self.jing_dian_ming_cheng
        }