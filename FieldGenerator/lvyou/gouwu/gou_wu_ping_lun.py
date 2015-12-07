# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class gou_wu_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.tuan_gou_gou_wu_ming = None
        self.ping_fen = None
        self.yong_hu_ming = None
        self.ping_lun_shi_jian = None
        self.ping_lun_nei_rong = None
        self.guo_jia_ming_cheng = None
        self.gou_wu_di_ming_cheng = None
        self.ping_fen_xing_ji = None
        self.dian_zan_shu_liang = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'团购购物名': self.tuan_gou_gou_wu_ming,
            u'评分': self.ping_fen,
            u'用户名': self.yong_hu_ming,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论内容': self.ping_lun_nei_rong,
            u'国家名称': self.guo_jia_ming_cheng,
            u'购物地名称': self.gou_wu_di_ming_cheng,
            u'评分星级': self.ping_fen_xing_ji,
            u'点赞数量': self.dian_zan_shu_liang
        }