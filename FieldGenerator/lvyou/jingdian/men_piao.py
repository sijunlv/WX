# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class men_piao(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.jing_dian_ming_cheng = None
        self.suo_shu_cheng_shi = None
        self.jing_qu_deng_ji = None
        self.xiao_liang = None
        self.jing_qu_dian_hua = None
        self.kai_fang_shi_jian = None
        self.zhu_ti_fen_lei = None
        self.jing_dian_di_zhi = None
        self.men_piao_ming_cheng = None
        self.shang_jia_xin_xi = None
        self.shang_pin_ming_cheng = None
        self.men_piao_lei_xing = None
        self.jia_ge = None
        self.re_du = None
        self.zong_he_ping_fen = None
        self.tian_qi_yu_bao = None
        self.yu_ding_wang_zhan = None
        self.chan_pin_shuo_ming = None
        self.jia_ge_xiang_qing = None
        self.guo_jia = None
        self.cheng_shi = None
        self.chu_fa_di = None
        self.mu_di_di = None
        self.er_tong_jia_ge = None
        self.dian_ping_zong_shu = None
        self.you_ke_man_yi_du = None
        self.fu_wu_cheng_nuo = None
        self.shou_cang_shu = None
        self.fen_lei = None
        self.sheng_shi = None
        self.ti_qian_yu_ding_shi_jian = None
        self.zhi_fu_fang_shi = None
        self.you_hui = None
        self.yuan_jia = None
        self.men_piao_te_dian = None
        self.ru_yuan_fang_shi = None
        self.men_piao_you_xiao_qi = None
        self.qi_ta_shuo_ming = None
        self.fan_xian_jin_quan = None
        self.men_piao_lei_xing_1 = None
        self.cheng_ren_piao_jia_ge = None
        self.lao_ren_piao_jia_ge = None
        self.xue_sheng_piao_jia_ge = None
        self.shi_jian = None
        self.wen_du = None
        self.tian_qi = None
        self.hao_ping_lv = None
        self.chan_pin_lei_xing = None

    def makemap(self):
        return {
            u'景点名称': self.jing_dian_ming_cheng,
            u'所属城市': self.suo_shu_cheng_shi,
            u'景区等级': self.jing_qu_deng_ji,
            u'销量': self.xiao_liang,
            u'景区电话': self.jing_qu_dian_hua,
            u'开放时间': self.kai_fang_shi_jian,
            u'主题分类': self.zhu_ti_fen_lei,
            u'景点地址': self.jing_dian_di_zhi,
            u'门票名称': self.men_piao_ming_cheng,
            u'商家信息': self.shang_jia_xin_xi,
            u'商品名称': self.shang_pin_ming_cheng,
            u'门票类型': self.men_piao_lei_xing,
            u'价格': self.jia_ge,
            u'热度': self.re_du,
            u'综合评分': self.zong_he_ping_fen,
            u'天气预报': self.tian_qi_yu_bao,
            u'预定网站': self.yu_ding_wang_zhan,
            u'产品说明': self.chan_pin_shuo_ming,
            u'价格详情': self.jia_ge_xiang_qing,
            u'国家': self.guo_jia,
            u'城市': self.cheng_shi,
            u'出发地': self.chu_fa_di,
            u'目的地': self.mu_di_di,
            u'儿童价格': self.er_tong_jia_ge,
            u'点评总数': self.dian_ping_zong_shu,
            u'游客满意度': self.you_ke_man_yi_du,
            u'服务承诺': self.fu_wu_cheng_nuo,
            u'收藏数': self.shou_cang_shu,
            u'分类': self.fen_lei,
            u'省市': self.sheng_shi,
            u'提前预定时间': self.ti_qian_yu_ding_shi_jian,
            u'支付方式': self.zhi_fu_fang_shi,
            u'优惠': self.you_hui,
            u'原价': self.yuan_jia,
            u'门票特点': self.men_piao_te_dian,
            u'入园方式': self.ru_yuan_fang_shi,
            u'门票有效期': self.men_piao_you_xiao_qi,
            u'其他说明': self.qi_ta_shuo_ming,
            u'返现金券': self.fan_xian_jin_quan,
            u'门票类型1': self.men_piao_lei_xing_1,
            u'成人票价格': self.cheng_ren_piao_jia_ge,
            u'老人票价格': self.lao_ren_piao_jia_ge,
            u'学生票价格': self.xue_sheng_piao_jia_ge,
            u'时间': self.shi_jian,
            u'温度': self.wen_du,
            u'天气': self.tian_qi,
            u'好评率': self.hao_ping_lv,
            u'产品类型': self.chan_pin_lei_xing
        }