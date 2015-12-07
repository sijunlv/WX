# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tuan_gou_mei_shi(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.tuan_gou_mei_shi_ming = None
        self.tuan_gou_mei_shi_nei_rong = None
        self.jia_ge = None
        self.jia_zhi = None
        self.yi_shou_fen_shu = None
        self.ping_fen = None
        self.ping_lun_shu_liang = None
        self.you_xiao_qi = None
        self.guo_jia_ming_cheng = None
        self.mei_shi_pai_ming = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'团购美食名': self.tuan_gou_mei_shi_ming,
            u'团购美食内容': self.tuan_gou_mei_shi_nei_rong,
            u'价格': self.jia_ge,
            u'价值': self.jia_zhi,
            u'已售份数': self.yi_shou_fen_shu,
            u'评分': self.ping_fen,
            u'评论数量': self.ping_lun_shu_liang,
            u'有效期': self.you_xiao_qi,
            u'国家名称': self.guo_jia_ming_cheng,
            u'美食排名': self.mei_shi_pai_ming
        }