# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tuan_gou_gou_wu(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.tuan_gou_gou_wu_ming = None
        self.tuan_gou_gou_wu_nei_rong = None
        self.jia_ge = None
        self.jia_zhi = None
        self.yi_shou_fen_shu = None
        self.ping_fen = None
        self.ping_lun_tiao_shu = None
        self.you_xian_qi = None
        self.guo_jia_ming_cheng = None
        self.gou_wu_di_ming_cheng = None
        self.pai_ming = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'团购购物名': self.tuan_gou_gou_wu_ming,
            u'团购购物内容': self.tuan_gou_gou_wu_nei_rong,
            u'价格': self.jia_ge,
            u'价值': self.jia_zhi,
            u'已售份数': self.yi_shou_fen_shu,
            u'评分': self.ping_fen,
            u'评论条数': self.ping_lun_tiao_shu,
            u'有限期': self.you_xian_qi,
            u'国家名称': self.guo_jia_ming_cheng,
            u'购物地名称': self.gou_wu_di_ming_cheng,
            u'排名': self.pai_ming
        }