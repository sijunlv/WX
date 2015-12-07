# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_jing_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.fen_lei = None
        self.jing_dian_ming = None
        self.ping_fen = None
        self.ren_jun = None
        self.di_zhi = None
        self.te_se = None
        self.ying_ye_shi_jian = None
        self.ting_che_xin_xi = None
        self.ping_fen_shu = None
        self.xiang_mu = None
        self.can_yin = None
        self.hua_suan = None
        self.yong_hu_ming = None
        self.gong_xian_zhi = None
        self.ping_lun_nei_rong = None
        self.ping_lun_shi_jian = None
        self.sheng_fen = None
        self.hao_ping_lv = None
        self.zhong_ping_lun = None
        self.cha_ping_lv = None
        self.xing_cheng_an_pai = None
        self.lv_xing_jiao_tong = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.you_tu_ping_lun_zong_shu = None
        self.hui_yuan_deng_ji = None
        self.chu_you_lei_xing = None
        self.ping_lun_lai_yuan = None
        self.you_yong_shu_liang = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'分类': self.fen_lei,
            u'景点名': self.jing_dian_ming,
            u'评分': self.ping_fen,
            u'人均': self.ren_jun,
            u'地址': self.di_zhi,
            u'特色': self.te_se,
            u'营业时间': self.ying_ye_shi_jian,
            u'停车信息': self.ting_che_xin_xi,
            u'评分数': self.ping_fen_shu,
            u'项目': self.xiang_mu,
            u'餐饮': self.can_yin,
            u'划算': self.hua_suan,
            u'用户名': self.yong_hu_ming,
            u'贡献值': self.gong_xian_zhi,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论时间': self.ping_lun_shi_jian,
            u'省份': self.sheng_fen,
            u'好评率': self.hao_ping_lv,
            u'中评论': self.zhong_ping_lun,
            u'差评率': self.cha_ping_lv,
            u'行程安排': self.xing_cheng_an_pai,
            u'旅行交通': self.lv_xing_jiao_tong,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'有图评论总数': self.you_tu_ping_lun_zong_shu,
            u'会员等级': self.hui_yuan_deng_ji,
            u'出游类型': self.chu_you_lei_xing,
            u'评论来源': self.ping_lun_lai_yuan,
            u'有用数量': self.you_yong_shu_liang
        }