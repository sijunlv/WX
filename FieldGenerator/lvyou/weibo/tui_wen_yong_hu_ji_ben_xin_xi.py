# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tui_wen_yong_hu_ji_ben_xin_xi(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.quan_ming = None
        self.yong_hu_ming = None
        self.ge_ren_jian_jie = None
        self.di_zhi = None
        self.wang_zhi = None
        self.zhu_ce_shi_jian = None
        self.chu_sheng_ri_qi = None
        self.zhang_hao_shi_fou_ren_zheng = None
        self.tui_wen_shu_liang = None
        self.guan_zhu_shu_liang = None
        self.bei_guan_zhu_shu_liang = None
        self.xi_huan_shu_liang = None
        self.lie_biao_shu_liang = None

    def makemap(self):
        return {
            u'全名': self.quan_ming,
            u'用户名': self.yong_hu_ming,
            u'个人简介': self.ge_ren_jian_jie,
            u'地址': self.di_zhi,
            u'网址': self.wang_zhi,
            u'注册时间': self.zhu_ce_shi_jian,
            u'出生日期': self.chu_sheng_ri_qi,
            u'账号是否认证': self.zhang_hao_shi_fou_ren_zheng,
            u'推文数量': self.tui_wen_shu_liang,
            u'关注数量': self.guan_zhu_shu_liang,
            u'被关注数量': self.bei_guan_zhu_shu_liang,
            u'喜欢数量': self.xi_huan_shu_liang,
            u'列表数量': self.lie_biao_shu_liang
        }