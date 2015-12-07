# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class yong_hu_dong_tai_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.yong_hu_ming = None
        self.fa_biao_shi_jian = None
        self.fa_biao_nei_rong = None
        self.dian_zan_shu_liang = None
        self.fen_xiang_ci_shu = None

    def makemap(self):
        return {
            u'用户名': self.yong_hu_ming,
            u'发表时间': self.fa_biao_shi_jian,
            u'发表内容': self.fa_biao_nei_rong,
            u'点赞数量': self.dian_zan_shu_liang,
            u'分享次数': self.fen_xiang_ci_shu
        }