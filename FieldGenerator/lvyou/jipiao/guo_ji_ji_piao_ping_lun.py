# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_ji_ji_piao_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.chu_xing_fang_shi = None
        self.yong_hu_ming = None
        self.hang_xian = None
        self.dui_tong_cheng_di_dian_ping = None
        self.dui_hang_si_di_dian_ping = None
        self.ping_lun_shi_jian = None
        self.you_yong_shu_liang = None

    def makemap(self):
        return {
            u'出行方式': self.chu_xing_fang_shi,
            u'用户名': self.yong_hu_ming,
            u'航线': self.hang_xian,
            u'对同程的点评': self.dui_tong_cheng_di_dian_ping,
            u'对航司的点评': self.dui_hang_si_di_dian_ping,
            u'评论时间': self.ping_lun_shi_jian,
            u'有用数量': self.you_yong_shu_liang
        }