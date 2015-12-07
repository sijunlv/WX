# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_ji_piao(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.chu_fa_cheng_shi = None
        self.dao_da_cheng_shi = None
        self.chu_fa_ri_qi = None
        self.hang_kong_gong_si = None
        self.ji_xing = None
        self.qi_fei_shi_jian = None
        self.jiang_luo_shi_jian = None
        self.qi_fei_ji_chang = None
        self.jiang_luo_ji_chang = None
        self.jia_ge = None
        self.zhe_kou = None
        self.hang_ban_hao = None
        self.ban_qi = None
        self.jing_ting = None
        self.can_shi = None
        self.zhun_dian_lv = None
        self.ping_lun_zong_shu = None
        self.ping_fen_xing_ji = None
        self.ping_lun_tiao_shu = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.hao_ping_lv = None
        self.zhong_ping_lv = None
        self.cha_ping_lv = None
        self.ke_fu_fu_wu = None
        self.zhi_fu_bian_jie = None
        self.chu_piao_su_du = None
        self.pai_ming = None
        self.hang_xian_ming = None
        self.ding_piao_wang_zhan = None
        self.tui_gai_zheng_ce = None
        self.ji_cang = None

    def makemap(self):
        return {
            u'出发城市': self.chu_fa_cheng_shi,
            u'到达城市': self.dao_da_cheng_shi,
            u'出发日期': self.chu_fa_ri_qi,
            u'航空公司': self.hang_kong_gong_si,
            u'机型': self.ji_xing,
            u'起飞时间': self.qi_fei_shi_jian,
            u'降落时间': self.jiang_luo_shi_jian,
            u'起飞机场': self.qi_fei_ji_chang,
            u'降落机场': self.jiang_luo_ji_chang,
            u'价格': self.jia_ge,
            u'折扣': self.zhe_kou,
            u'航班号': self.hang_ban_hao,
            u'班期': self.ban_qi,
            u'经停': self.jing_ting,
            u'餐食': self.can_shi,
            u'准点率': self.zhun_dian_lv,
            u'评论总数': self.ping_lun_zong_shu,
            u'评分星级': self.ping_fen_xing_ji,
            u'评论条数': self.ping_lun_tiao_shu,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'好评率': self.hao_ping_lv,
            u'中评率': self.zhong_ping_lv,
            u'差评率': self.cha_ping_lv,
            u'客服服务': self.ke_fu_fu_wu,
            u'支付便捷': self.zhi_fu_bian_jie,
            u'出票速度': self.chu_piao_su_du,
            u'排名': self.pai_ming,
            u'航线名': self.hang_xian_ming,
            u'订票网站': self.ding_piao_wang_zhan,
            u'退改政策': self.tui_gai_zheng_ce,
            u'机舱': self.ji_cang
        }