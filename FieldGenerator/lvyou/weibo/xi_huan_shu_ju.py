# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class xi_huan_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.xi_huan_yong_hu_quan_ming = None
        self.fa_tui_yong_hu_quan_ming = None
        self.fa_tui_yong_hu_ming = None
        self.fa_tui_shi_jian = None
        self.fa_tui_nei_rong = None
        self.zhuan_tui_shu_liang = None
        self.xi_huan_shu_liang = None

    def makemap(self):
        return {
            u'喜欢用户全名': self.xi_huan_yong_hu_quan_ming,
            u'发推用户全名': self.fa_tui_yong_hu_quan_ming,
            u'发推用户名': self.fa_tui_yong_hu_ming,
            u'发推时间': self.fa_tui_shi_jian,
            u'发推内容': self.fa_tui_nei_rong,
            u'转推数量': self.zhuan_tui_shu_liang,
            u'喜欢数量': self.xi_huan_shu_liang
        }