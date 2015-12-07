# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_ji_piao_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.ping_lun_shi_jian = None
        self.hao_ping_lei_xing = None
        self.dian_ping_hang_xian = None
        self.dui_tong_cheng_fu_wu = None
        self.dui_hang_kong_gong_si_ji_ji_chang = None
        self.ping_lun_lai_yuan = None

    def makemap(self):
        return {
            u'评论时间': self.ping_lun_shi_jian,
            u'好评类型': self.hao_ping_lei_xing,
            u'点评航线': self.dian_ping_hang_xian,
            u'对同程服务': self.dui_tong_cheng_fu_wu,
            u'对航空公司及机场': self.dui_hang_kong_gong_si_ji_ji_chang,
            u'评论来源': self.ping_lun_lai_yuan
        }