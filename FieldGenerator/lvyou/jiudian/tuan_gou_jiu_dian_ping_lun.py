# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class tuan_gou_jiu_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.tuan_gou_jiu_dian_ming = None
        self.jia_ge = None
        self.yi_shou_fen_shu = None
        self.ping_lun_tiao_shu = None
        self.you_xiao_qi = None
        self.sheng_fen = None
        self.zong_he_ping_fen = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.zhui_jia_ping_lun_zong_shu = None
        self.yong_hu_ming = None
        self.wei_sheng_ping_fen = None
        self.she_shi_ping_fen = None
        self.fu_wu_ping_fen = None
        self.xing_jia_bi_ping_fen = None
        self.ping_lun_nei_rong = None
        self.ping_lun_shi_jian = None
        self.tuan_gou_lei_xing = None
        self.qu_xian = None
        self.shang_ye_quan = None
        self.shi_yong_shi_jian = None
        self.yu_yue_ti_shi = None
        self.zhi_chi_you_hui = None
        self.hui_yuan_jue_se = None
        self.hui_yuan_deng_ji = None
        self.zhuan_jia_dian_ping_shu_liang = None
        self.zu_ji_shu_liang = None
        self.ping_lun_guan_jian_ci = None
        self.ru_zhu_lei_xing = None
        self.ping_lun_lai_yuan = None
        self.you_yong_shu_liang = None
        self.yong_hu_man_yi_du = None
        self.wei_zhi_jiao_tong = None
        self.xing_jia_bi = None
        self.she_shi_zhuang_huang = None
        self.wei_sheng_fu_wu = None
        self.zhu_su_lei_xing = None
        self.hao_ping_lei_xing = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'团购酒店名': self.tuan_gou_jiu_dian_ming,
            u'价格': self.jia_ge,
            u'已售份数': self.yi_shou_fen_shu,
            u'评论条数': self.ping_lun_tiao_shu,
            u'有效期': self.you_xiao_qi,
            u'省份': self.sheng_fen,
            u'综合评分': self.zong_he_ping_fen,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'追加评论总数': self.zhui_jia_ping_lun_zong_shu,
            u'用户名': self.yong_hu_ming,
            u'卫生评分': self.wei_sheng_ping_fen,
            u'设施评分': self.she_shi_ping_fen,
            u'服务评分': self.fu_wu_ping_fen,
            u'性价比评分': self.xing_jia_bi_ping_fen,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论时间': self.ping_lun_shi_jian,
            u'团购类型': self.tuan_gou_lei_xing,
            u'区县': self.qu_xian,
            u'商业圈': self.shang_ye_quan,
            u'使用时间': self.shi_yong_shi_jian,
            u'预约提示': self.yu_yue_ti_shi,
            u'支持优惠': self.zhi_chi_you_hui,
            u'会员角色': self.hui_yuan_jue_se,
            u'会员等级': self.hui_yuan_deng_ji,
            u'砖家点评数量': self.zhuan_jia_dian_ping_shu_liang,
            u'足迹数量': self.zu_ji_shu_liang,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'入住类型': self.ru_zhu_lei_xing,
            u'评论来源': self.ping_lun_lai_yuan,
            u'有用数量': self.you_yong_shu_liang,
            u'用户满意度': self.yong_hu_man_yi_du,
            u'位置交通': self.wei_zhi_jiao_tong,
            u'性价比': self.xing_jia_bi,
            u'设施装潢': self.she_shi_zhuang_huang,
            u'卫生服务': self.wei_sheng_fu_wu,
            u'住宿类型': self.zhu_su_lei_xing,
            u'好评类型': self.hao_ping_lei_xing
        }