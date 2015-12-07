# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tuan_gou_jing_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.jing_dian_ming = None
        self.jing_dian_nei_rong = None
        self.jia_ge = None
        self.jia_zhi = None
        self.yi_shou_fen_shu = None
        self.ping_fen = None
        self.ping_lun_tiao_shu = None
        self.you_xiao_qi = None
        self.tuan_gou_lei_xing = None
        self.sheng_shi = None
        self.gong_ying_shang = None
        self.can_tuan_ren_shu = None
        self.bian_hao = None
        self.xing_cheng_tian_shu = None
        self.wang_fan_jiao_tong = None
        self.chu_fa_shi_qi = None
        self.chan_pin_te_se = None
        self.zhe_kou = None
        self.hao_ping_lv = None
        self.fen_lei = None
        self.chu_fa_cheng_shi = None
        self.shou_cang_shu = None
        self.mu_di_di = None
        self.sheng_yu = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'景点名': self.jing_dian_ming,
            u'景点内容': self.jing_dian_nei_rong,
            u'价格': self.jia_ge,
            u'价值': self.jia_zhi,
            u'已售份数': self.yi_shou_fen_shu,
            u'评分': self.ping_fen,
            u'评论条数': self.ping_lun_tiao_shu,
            u'有效期': self.you_xiao_qi,
            u'团购类型': self.tuan_gou_lei_xing,
            u'省市': self.sheng_shi,
            u'供应商': self.gong_ying_shang,
            u'参团人数': self.can_tuan_ren_shu,
            u'编号': self.bian_hao,
            u'行程天数': self.xing_cheng_tian_shu,
            u'往返交通': self.wang_fan_jiao_tong,
            u'出发时期': self.chu_fa_shi_qi,
            u'产品特色': self.chan_pin_te_se,
            u'折扣': self.zhe_kou,
            u'好评率': self.hao_ping_lv,
            u'分类': self.fen_lei,
            u'出发城市': self.chu_fa_cheng_shi,
            u'收藏数': self.shou_cang_shu,
            u'目的地': self.mu_di_di,
            u'剩余': self.sheng_yu
        }