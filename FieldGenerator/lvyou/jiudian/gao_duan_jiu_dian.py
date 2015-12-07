# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class gao_duan_jiu_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.jiu_dian_lei_xing = None
        self.cheng_shi = None
        self.lian_suo_pin_pai = None
        self.jiu_dian_ming_cheng = None
        self.jiu_dian_ji_bie = None
        self.xiang_xi_di_zhi = None
        self.zong_he_ping_fen = None
        self.jiu_dian_pai_ming = None
        self.dian_ping_zong_shu = None
        self.kai_ye_shi_jian = None
        self.zui_jin_zhuang_xiu = None
        self.fang_jian_zong_shu = None
        self.ru_zhu_shi_jian = None
        self.li_dian_shi_jian = None
        self.fang_xing = None
        self.ru_zhu_ren_shu = None
        self.mian_ji = None
        self.lou_ceng = None
        self.she_shi = None
        self.yu_ding_wang_zhan = None
        self.zong_he_ping_ji = None
        self.yu_ding_xiang_qing = None
        self.jun_jia = None

    def makemap(self):
        return {
            u'酒店类型': self.jiu_dian_lei_xing,
            u'城市': self.cheng_shi,
            u'连锁品牌': self.lian_suo_pin_pai,
            u'酒店名称': self.jiu_dian_ming_cheng,
            u'酒店级别': self.jiu_dian_ji_bie,
            u'详细地址': self.xiang_xi_di_zhi,
            u'综合评分': self.zong_he_ping_fen,
            u'酒店排名': self.jiu_dian_pai_ming,
            u'点评总数': self.dian_ping_zong_shu,
            u'开业时间': self.kai_ye_shi_jian,
            u'最近装修': self.zui_jin_zhuang_xiu,
            u'房间总数': self.fang_jian_zong_shu,
            u'入住时间': self.ru_zhu_shi_jian,
            u'离店时间': self.li_dian_shi_jian,
            u'房型': self.fang_xing,
            u'入住人数': self.ru_zhu_ren_shu,
            u'面积': self.mian_ji,
            u'楼层': self.lou_ceng,
            u'设施': self.she_shi,
            u'预订网站': self.yu_ding_wang_zhan,
            u'综合评级': self.zong_he_ping_ji,
            u'预订详情': self.yu_ding_xiang_qing,
            u'均价': self.jun_jia
        }