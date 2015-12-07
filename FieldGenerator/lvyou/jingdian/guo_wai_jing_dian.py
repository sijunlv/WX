# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_wai_jing_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.fen_lei = None
        self.jing_dian_ming = None
        self.shang_hu_ren_zheng = None
        self.shang_hu_ping_fen = None
        self.ping_fen = None
        self.ping_lun_shu = None
        self.ren_jun = None
        self.di_zhi = None
        self.te_se = None
        self.ying_ye_shi_jian = None
        self.ting_che_xin_xi = None
        self.sheng_fen = None
        self.di_qu = None
        self.ji_bie = None
        self.jing_qu_rong_yu = None
        self.jian_yi_you_wan_shi_jian = None
        self.zui_jia_lv_you_shi_jie = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'分类': self.fen_lei,
            u'景点名': self.jing_dian_ming,
            u'商户认证': self.shang_hu_ren_zheng,
            u'商户评分': self.shang_hu_ping_fen,
            u'评分': self.ping_fen,
            u'评论数': self.ping_lun_shu,
            u'人均': self.ren_jun,
            u'地址': self.di_zhi,
            u'特色': self.te_se,
            u'营业时间': self.ying_ye_shi_jian,
            u'停车信息': self.ting_che_xin_xi,
            u'省份': self.sheng_fen,
            u'地区': self.di_qu,
            u'级别': self.ji_bie,
            u'景区荣誉': self.jing_qu_rong_yu,
            u'建议游玩时间': self.jian_yi_you_wan_shi_jian,
            u'最佳旅游时节': self.zui_jia_lv_you_shi_jie
        }