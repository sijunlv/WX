# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_gou_wu(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.fen_lei = None
        self.dian_ming = None
        self.shang_cheng_di_zhi = None
        self.ying_ye_shi_jian = None
        self.ting_che_xin_xi = None
        self.yong_hu_ping_ji = None
        self.ren_jun_xiao_fei = None
        self.chan_pin = None
        self.huan_jing = None
        self.fu_wu = None
        self.pai_ming = None
        self.shang_hu = None
        self.shang_qu = None
        self.ren_jun = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'分类': self.fen_lei,
            u'店名': self.dian_ming,
            u'商城地址': self.shang_cheng_di_zhi,
            u'营业时间': self.ying_ye_shi_jian,
            u'停车信息': self.ting_che_xin_xi,
            u'用户评级': self.yong_hu_ping_ji,
            u'人均消费': self.ren_jun_xiao_fei,
            u'产品': self.chan_pin,
            u'环境': self.huan_jing,
            u'服务': self.fu_wu,
            u'排名': self.pai_ming,
            u'商户': self.shang_hu,
            u'商区': self.shang_qu,
            u'人均': self.ren_jun
        }