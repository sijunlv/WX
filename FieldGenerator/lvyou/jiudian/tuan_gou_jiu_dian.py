# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tuan_gou_jiu_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.tuan_gou_jiu_dian_ming = None
        self.tuan_gou_jiu_dian_nei_rong = None
        self.jia_ge = None
        self.jia_zhi = None
        self.yi_shou_fen_shu = None
        self.ping_lun_tiao_shu = None
        self.you_xiao_qi = None
        self.sheng_fen = None
        self.xiang_xi_di_zhi = None
        self.zong_he_ping_fen = None
        self.ti_huo_fang_shi = None
        self.ku_cun_yu_liang = None
        self.tuan_gou_lei_xing = None
        self.xing_ji = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'团购酒店名': self.tuan_gou_jiu_dian_ming,
            u'团购酒店内容': self.tuan_gou_jiu_dian_nei_rong,
            u'价格': self.jia_ge,
            u'价值': self.jia_zhi,
            u'已售份数': self.yi_shou_fen_shu,
            u'评论条数': self.ping_lun_tiao_shu,
            u'有效期': self.you_xiao_qi,
            u'省份': self.sheng_fen,
            u'详细地址': self.xiang_xi_di_zhi,
            u'综合评分': self.zong_he_ping_fen,
            u'提货方式': self.ti_huo_fang_shi,
            u'库存余量': self.ku_cun_yu_liang,
            u'团购类型': self.tuan_gou_lei_xing,
            u'星级': self.xing_ji
        }