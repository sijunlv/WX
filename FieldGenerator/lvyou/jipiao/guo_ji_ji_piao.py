# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_ji_ji_piao(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.chu_fa_cheng_shi = None
        self.dao_da_cheng_shi = None
        self.chu_fa_shi_jian = None
        self.hang_kong_gong_si = None
        self.ji_xing = None
        self.qi_fei_shi_jian = None
        self.dao_da_shi_jian = None
        self.qi_fei_ji_chang = None
        self.dao_da_ji_chang = None
        self.lv_xing_zong_shi_chang = None
        self.zhi_fei_tui_jian_biao_qian = None
        self.ji_piao_piao_jia = None
        self.qi_ta_fei_yong = None
        self.hang_ban_hao = None
        self.ban_qi = None
        self.jing_ting = None
        self.can_shi = None
        self.zhun_dian_lv = None
        self.ping_fen_xing_ji = None
        self.ke_hu_man_yi_du = None
        self.ping_lun_zong_shu = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.hang_xian = None
        self.ding_piao_wang_zhan = None

    def makemap(self):
        return {
            u'出发城市': self.chu_fa_cheng_shi,
            u'到达城市': self.dao_da_cheng_shi,
            u'出发时间': self.chu_fa_shi_jian,
            u'航空公司': self.hang_kong_gong_si,
            u'机型': self.ji_xing,
            u'起飞时间': self.qi_fei_shi_jian,
            u'到达时间': self.dao_da_shi_jian,
            u'起飞机场': self.qi_fei_ji_chang,
            u'到达机场': self.dao_da_ji_chang,
            u'旅行总时长': self.lv_xing_zong_shi_chang,
            u'直飞推荐标签': self.zhi_fei_tui_jian_biao_qian,
            u'机票票价': self.ji_piao_piao_jia,
            u'其他费用': self.qi_ta_fei_yong,
            u'航班号': self.hang_ban_hao,
            u'班期': self.ban_qi,
            u'经停': self.jing_ting,
            u'餐食': self.can_shi,
            u'准点率': self.zhun_dian_lv,
            u'评分星级': self.ping_fen_xing_ji,
            u'客户满意度': self.ke_hu_man_yi_du,
            u'评论总数': self.ping_lun_zong_shu,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'航线': self.hang_xian,
            u'订票网站': self.ding_piao_wang_zhan
        }