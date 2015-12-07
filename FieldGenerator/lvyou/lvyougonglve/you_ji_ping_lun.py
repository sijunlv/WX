# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class you_ji_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.you_ji_biao_ti = None
        self.you_ji_zuo_zhe = None
        self.deng_ji = None
        self.fa_biao_shi_jian = None
        self.yong_hu_ming = None
        self.ping_lun_nei_rong = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'游记标题': self.you_ji_biao_ti,
            u'游记作者': self.you_ji_zuo_zhe,
            u'等级': self.deng_ji,
            u'发表时间': self.fa_biao_shi_jian,
            u'用户名': self.yong_hu_ming,
            u'评论内容': self.ping_lun_nei_rong
        }