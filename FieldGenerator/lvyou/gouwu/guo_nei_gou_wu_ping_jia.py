# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_gou_wu_ping_jia(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.dian_ming = None
        self.chan_pin = None
        self.huan_jing = None
        self.fu_wu = None
        self.yong_hu_ming = None
        self.gong_xian_zhi = None
        self.ping_fen = None
        self.nei_rong = None
        self.ting_che_xin_xi = None
        self.ping_lun_shi_jian = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'店名': self.dian_ming,
            u'产品': self.chan_pin,
            u'环境': self.huan_jing,
            u'服务': self.fu_wu,
            u'用户名': self.yong_hu_ming,
            u'贡献值': self.gong_xian_zhi,
            u'评分': self.ping_fen,
            u'内容': self.nei_rong,
            u'停车信息': self.ting_che_xin_xi,
            u'评论时间': self.ping_lun_shi_jian
        }