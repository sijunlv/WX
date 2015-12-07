# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class lv_guan(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.mu_di_di = None
        self.lv_guan_ming = None
        self.xiang_xi_di_zhi = None
        self.liu_lan_liang = None
        self.ping_lun_shu = None
        self.zui_duo_rong_na_ren_shu = None
        self.jia_ge = None
        self.yong_hu_ming = None
        self.ping_lun_shi_jian = None
        self.nei_rong = None
        self.qu_yu = None
        self.zong_he_ping_fen = None
        self.xiao_liang = None
        self.ru_zhu_shi_jian = None
        self.li_dian_shi_jian = None
        self.fang_xing = None
        self.chuang_xing = None
        self.shang_wang_fang_shi = None
        self.mian_ji = None
        self.lou_ceng = None
        self.mai_jia = None
        self.chu_li_shi_chang = None
        self.yu_ding_cheng_gong_lv = None
        self.yu_ding_xiang_qing = None
        self.ping_lun_guan_jian_ci = None
        self.chu_zu_fang_shi = None
        self.shang_ye_quan = None
        self.sheng_yu_liang = None
        self.you_hui = None
        self.hui_yuan_zhe_kou = None
        self.fu_kuan_fang_shi = None
        self.fang_wu_bian_hao = None
        self.fang_wu_gui_ge = None
        self.chuang_di_shu_liang = None
        self.shi_fou_you_wang_luo = None

    def makemap(self):
        return {
            u'目的地': self.mu_di_di,
            u'旅馆名': self.lv_guan_ming,
            u'详细地址': self.xiang_xi_di_zhi,
            u'浏览量': self.liu_lan_liang,
            u'评论数': self.ping_lun_shu,
            u'最多容纳人数': self.zui_duo_rong_na_ren_shu,
            u'价格': self.jia_ge,
            u'用户名': self.yong_hu_ming,
            u'评论时间': self.ping_lun_shi_jian,
            u'内容': self.nei_rong,
            u'区域': self.qu_yu,
            u'综合评分': self.zong_he_ping_fen,
            u'销量': self.xiao_liang,
            u'入住时间': self.ru_zhu_shi_jian,
            u'离店时间': self.li_dian_shi_jian,
            u'房型': self.fang_xing,
            u'床型': self.chuang_xing,
            u'上网方式': self.shang_wang_fang_shi,
            u'面积': self.mian_ji,
            u'楼层': self.lou_ceng,
            u'卖家': self.mai_jia,
            u'处理时长': self.chu_li_shi_chang,
            u'预订成功率': self.yu_ding_cheng_gong_lv,
            u'预订详情': self.yu_ding_xiang_qing,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'出租方式': self.chu_zu_fang_shi,
            u'商业圈': self.shang_ye_quan,
            u'剩余量': self.sheng_yu_liang,
            u'优惠': self.you_hui,
            u'会员折扣': self.hui_yuan_zhe_kou,
            u'付款方式': self.fu_kuan_fang_shi,
            u'房屋编号': self.fang_wu_bian_hao,
            u'房屋规格': self.fang_wu_gui_ge,
            u'床的数量': self.chuang_di_shu_liang,
            u'是否有网络': self.shi_fou_you_wang_luo
        }