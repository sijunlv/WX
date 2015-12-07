# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_mei_shi(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.fen_lei = None
        self.dian_ming = None
        self.shang_hu_ren_zheng = None
        self.shang_hu_ping_fen = None
        self.ping_lun_shu = None
        self.ren_jun = None
        self.di_zhi = None
        self.te_se = None
        self.ying_ye_shi_jian = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'分类': self.fen_lei,
            u'店名': self.dian_ming,
            u'商户认证': self.shang_hu_ren_zheng,
            u'商户评分': self.shang_hu_ping_fen,
            u'评论数': self.ping_lun_shu,
            u'人均': self.ren_jun,
            u'地址': self.di_zhi,
            u'特色': self.te_se,
            u'营业时间': self.ying_ye_shi_jian
        }