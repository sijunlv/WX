# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class you_hui_ji_ben_xin_xi(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.fen_lei = None
        self.lei_xing = None
        self.ming_cheng = None
        self.jia_ge = None
        self.nei_rong = None
        self.you_xiao_qi = None
        self.liu_lan_shu = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'分类': self.fen_lei,
            u'类型': self.lei_xing,
            u'名称': self.ming_cheng,
            u'价格': self.jia_ge,
            u'内容': self.nei_rong,
            u'有效期': self.you_xiao_qi,
            u'浏览数': self.liu_lan_shu
        }