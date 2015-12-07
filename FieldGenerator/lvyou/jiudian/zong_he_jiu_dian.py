# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class zong_he_jiu_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.di_qu = None
        self.cheng_shi = None
        self.jiu_dian_ming_cheng = None
        self.jiu_dian_xing_ji = None
        self.xiang_xi_di_zhi = None
        self.jia_ge = None
        self.qu_yu = None
        self.ke_fang_shu = None
        self.zong_he_ping_fen = None
        self.dian_ping_zong_shu = None
        self.yong_hu_ming = None
        self.ping_lun_shi_jian = None
        self.ping_lun_nei_rong = None
        self.ying_wen_ming = None
        self.tui_jian_lv = None
        self.shi_fou_can_jia_shou_xuan_zhu_su = None
        self.zhe_kou_lv = None
        self.ru_zhu_ri_qi = None
        self.tui_fang_ri_qi = None
        self.fang_xing = None
        self.ke_fang_yu_liang = None
        self.shi_fou_you_chao_zhi_you_hui = None
        self.zui_duo_ren_shu = None
        self.tui_ding_zheng_ce = None
        self.shi_fou_han_zao = None
        self.da_gai_miao_shu = None
        self.chu_xing_mu_di = None
        self.chu_xing_ren_qun = None
        self.ru_zhu_tian_shu = None
        self.ping_lun_lai_yuan = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'地区': self.di_qu,
            u'城市': self.cheng_shi,
            u'酒店名称': self.jiu_dian_ming_cheng,
            u'酒店星级': self.jiu_dian_xing_ji,
            u'详细地址': self.xiang_xi_di_zhi,
            u'价格': self.jia_ge,
            u'区域': self.qu_yu,
            u'客房数': self.ke_fang_shu,
            u'综合评分': self.zong_he_ping_fen,
            u'点评总数': self.dian_ping_zong_shu,
            u'用户名': self.yong_hu_ming,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论内容': self.ping_lun_nei_rong,
            u'英文名': self.ying_wen_ming,
            u'推荐率': self.tui_jian_lv,
            u'是否参加首选住宿': self.shi_fou_can_jia_shou_xuan_zhu_su,
            u'折扣率': self.zhe_kou_lv,
            u'入住日期': self.ru_zhu_ri_qi,
            u'退房日期': self.tui_fang_ri_qi,
            u'房型': self.fang_xing,
            u'客房余量': self.ke_fang_yu_liang,
            u'是否有超值优惠': self.shi_fou_you_chao_zhi_you_hui,
            u'最多人数': self.zui_duo_ren_shu,
            u'退订政策': self.tui_ding_zheng_ce,
            u'是否含早': self.shi_fou_han_zao,
            u'大概描述': self.da_gai_miao_shu,
            u'出行目的': self.chu_xing_mu_di,
            u'出行人群': self.chu_xing_ren_qun,
            u'入住天数': self.ru_zhu_tian_shu,
            u'评论来源': self.ping_lun_lai_yuan
        }