# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class lv_guan_ping_jia(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.mu_di_di = None
        self.lv_guan_ming = None
        self.xiang_xi_di_zhi = None
        self.yong_hu_ming = None
        self.ping_lun_shi_jian = None
        self.nei_rong = None
        self.qu_yu = None
        self.zong_he_ping_fen = None
        self.ru_zhu_shi_jian = None
        self.fang_xing = None
        self.wei_sheng_ping_fen = None
        self.she_shi_ping_fen = None
        self.fu_wu_ping_fen = None
        self.xing_jia_bi_ping_fen = None
        self.ping_lun_nei_rong = None
        self.ping_lun_guan_jian_ci = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.chu_you_ren_qun = None
        self.da_zhi_miao_shu = None
        self.jiao_tong_wei_zhi_ping_fen = None

    def makemap(self):
        return {
            u'目的地': self.mu_di_di,
            u'旅馆名': self.lv_guan_ming,
            u'详细地址': self.xiang_xi_di_zhi,
            u'用户名': self.yong_hu_ming,
            u'评论时间': self.ping_lun_shi_jian,
            u'内容': self.nei_rong,
            u'区域': self.qu_yu,
            u'综合评分': self.zong_he_ping_fen,
            u'入住时间': self.ru_zhu_shi_jian,
            u'房型': self.fang_xing,
            u'卫生评分': self.wei_sheng_ping_fen,
            u'设施评分': self.she_shi_ping_fen,
            u'服务评分': self.fu_wu_ping_fen,
            u'性价比评分': self.xing_jia_bi_ping_fen,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'出游人群': self.chu_you_ren_qun,
            u'大致描述': self.da_zhi_miao_shu,
            u'交通位置评分': self.jiao_tong_wei_zhi_ping_fen
        }