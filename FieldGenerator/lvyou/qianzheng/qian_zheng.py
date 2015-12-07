# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class qian_zheng(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.chan_pin_ming_cheng = None
        self.xiao_liang = None
        self.ping_jia_zong_shu = None
        self.qian_zheng_guo_jia = None
        self.dai_ban_qian_zheng_lei_xing = None
        self.qian_zheng_lei_xing = None
        self.hu_zhao_qian_fa_di_chang_zhu_di = None
        self.qian_zheng_tao_can = None
        self.zong_he_ping_fen = None
        self.xiao_shou_dian_pu = None
        self.ping_lun_nei_rong = None
        self.ping_lun_shi_jian = None
        self.yong_hu_ming = None
        self.xing_hao = None
        self.shu_liang = None
        self.cheng_jiao_shi_jian = None
        self.chan_pin_bian_hao = None
        self.qian_zheng_mu_di_di = None
        self.huo_dong_xin_xi = None
        self.ti_qian_yu_ding_tian_shu = None
        self.bao_zheng_jin = None
        self.shi_fou_mian_shi = None
        self.jia_ge = None
        self.ru_jing_ci_shu = None
        self.you_xiao_qi = None
        self.zui_chang_ting_liu = None
        self.ban_li_shi_chang = None
        self.man_yi_du = None
        self.chu_qian_lv = None
        self.ling_qu = None
        self.liu_lan_ci_shu = None
        self.ping_lun_lai_yuan = None
        self.lv_you_zi_xun = None
        self.hui_fu = None
        self.zi_xun_shi_jian = None
        self.qu_yu = None
        self.liu_lan_zong_liang = None
        self.zong_he_chu_qian_lv = None

    def makemap(self):
        return {
            u'产品名称': self.chan_pin_ming_cheng,
            u'销量': self.xiao_liang,
            u'评价总数': self.ping_jia_zong_shu,
            u'签证国家': self.qian_zheng_guo_jia,
            u'代办签证类型': self.dai_ban_qian_zheng_lei_xing,
            u'签证类型': self.qian_zheng_lei_xing,
            u'护照签发地/常住地': self.hu_zhao_qian_fa_di_chang_zhu_di,
            u'签证套餐': self.qian_zheng_tao_can,
            u'综合评分': self.zong_he_ping_fen,
            u'销售店铺': self.xiao_shou_dian_pu,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论时间': self.ping_lun_shi_jian,
            u'用户名': self.yong_hu_ming,
            u'型号': self.xing_hao,
            u'数量': self.shu_liang,
            u'成交时间': self.cheng_jiao_shi_jian,
            u'产品编号': self.chan_pin_bian_hao,
            u'签证目的地': self.qian_zheng_mu_di_di,
            u'活动信息': self.huo_dong_xin_xi,
            u'提前预定天数': self.ti_qian_yu_ding_tian_shu,
            u'保证金': self.bao_zheng_jin,
            u'是否面试': self.shi_fou_mian_shi,
            u'价格': self.jia_ge,
            u'入境次数': self.ru_jing_ci_shu,
            u'有效期': self.you_xiao_qi,
            u'最长停留': self.zui_chang_ting_liu,
            u'办理时长': self.ban_li_shi_chang,
            u'满意度': self.man_yi_du,
            u'出签率': self.chu_qian_lv,
            u'领区': self.ling_qu,
            u'浏览次数': self.liu_lan_ci_shu,
            u'评论来源': self.ping_lun_lai_yuan,
            u'旅游咨询': self.lv_you_zi_xun,
            u'回复': self.hui_fu,
            u'咨询时间': self.zi_xun_shi_jian,
            u'区域': self.qu_yu,
            u'浏览总量': self.liu_lan_zong_liang,
            u'综合出签率': self.zong_he_chu_qian_lv
        }