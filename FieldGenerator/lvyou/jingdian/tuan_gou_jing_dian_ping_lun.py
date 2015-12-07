# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tuan_gou_jing_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.jing_dian_ming = None
        self.ping_fen = None
        self.yong_hu_ming = None
        self.ping_lun_shi_jian = None
        self.ping_lun_nei_rong = None
        self.fen_lei = None
        self.chu_fa_cheng_shi = None
        self.deng_ji = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'景点名': self.jing_dian_ming,
            u'评分': self.ping_fen,
            u'用户名': self.yong_hu_ming,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论内容': self.ping_lun_nei_rong,
            u'分类': self.fen_lei,
            u'出发城市': self.chu_fa_cheng_shi,
            u'等级': self.deng_ji
        }