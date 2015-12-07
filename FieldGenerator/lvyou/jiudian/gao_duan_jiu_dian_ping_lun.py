# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class gao_duan_jiu_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.jiu_dian_lei_xing = None
        self.cheng_shi = None
        self.lian_suo_pin_pai = None
        self.jiu_dian_ming_cheng = None
        self.zong_he_ping_fen = None
        self.ru_zhu_shi_jian = None
        self.dian_ping_zong_shu = None
        self.wen_da_zong_shu = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.yong_hu_ming = None
        self.hui_yuan_jue_se = None
        self.hui_yuan_deng_ji = None
        self.zhuan_jia_dian_ping_shu_liang = None
        self.zu_ji_shu_liang = None
        self.ping_lun_guan_jian_ci = None
        self.ping_lun_nei_rong = None
        self.ru_zhu_lei_xing = None
        self.ping_lun_lai_yuan = None
        self.you_yong_shu_liang = None

    def makemap(self):
        return {
            u'酒店类型': self.jiu_dian_lei_xing,
            u'城市': self.cheng_shi,
            u'连锁品牌': self.lian_suo_pin_pai,
            u'酒店名称': self.jiu_dian_ming_cheng,
            u'综合评分': self.zong_he_ping_fen,
            u'入住时间': self.ru_zhu_shi_jian,
            u'点评总数': self.dian_ping_zong_shu,
            u'问答总数': self.wen_da_zong_shu,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'用户名': self.yong_hu_ming,
            u'会员角色': self.hui_yuan_jue_se,
            u'会员等级': self.hui_yuan_deng_ji,
            u'砖家点评数量': self.zhuan_jia_dian_ping_shu_liang,
            u'足迹数量': self.zu_ji_shu_liang,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'评论内容': self.ping_lun_nei_rong,
            u'入住类型': self.ru_zhu_lei_xing,
            u'评论来源': self.ping_lun_lai_yuan,
            u'有用数量': self.you_yong_shu_liang
        }