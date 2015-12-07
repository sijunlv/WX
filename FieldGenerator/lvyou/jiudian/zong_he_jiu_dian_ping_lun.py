# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class zong_he_jiu_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.di_qu = None
        self.cheng_shi = None
        self.jiu_dian_ming_cheng = None
        self.zui_xin_dian_ping = None
        self.shang_wu_lv_ke = None
        self.fu_fu = None
        self.dan_xing_lv_ke = None
        self.jia_ting_ji_er_tong = None
        self.jia_ting_da_ling_er_tong = None
        self.tuan_dui_you_ke = None
        self.zong_he_ying_xiang = None
        self.zong_he_ping_fen = None
        self.dian_ping_zong_shu = None
        self.xing_jia_bi = None
        self.wei_zhi = None
        self.fu_wu = None
        self.huan_jing_he_qing_jie_du = None
        self.ke_fang_shu_shi_du = None
        self.yong_hu_ming = None
        self.ke_hu_lei_xing = None
        self.ping_lun_shi_jian = None
        self.ping_lun_nei_rong = None
        self.ping_fen = None
        self.ying_wen_ming = None
        self.tui_jian_lv = None
        self.jiu_dian_tiao_jian = None
        self.shi_fou_tui_jian = None
        self.lei_bie = None
        self.fa_bu = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'地区': self.di_qu,
            u'城市': self.cheng_shi,
            u'酒店名称': self.jiu_dian_ming_cheng,
            u'最新点评': self.zui_xin_dian_ping,
            u'商务旅客': self.shang_wu_lv_ke,
            u'夫妇': self.fu_fu,
            u'单行旅客': self.dan_xing_lv_ke,
            u'家庭及儿童': self.jia_ting_ji_er_tong,
            u'家庭大龄儿童': self.jia_ting_da_ling_er_tong,
            u'团队游客': self.tuan_dui_you_ke,
            u'综合映像': self.zong_he_ying_xiang,
            u'综合评分': self.zong_he_ping_fen,
            u'点评总数': self.dian_ping_zong_shu,
            u'性价比': self.xing_jia_bi,
            u'位置': self.wei_zhi,
            u'服务': self.fu_wu,
            u'环境和清洁度': self.huan_jing_he_qing_jie_du,
            u'客房舒适度': self.ke_fang_shu_shi_du,
            u'用户名': self.yong_hu_ming,
            u'客户类型': self.ke_hu_lei_xing,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论内容': self.ping_lun_nei_rong,
            u'评分': self.ping_fen,
            u'英文名': self.ying_wen_ming,
            u'推荐率': self.tui_jian_lv,
            u'酒店条件': self.jiu_dian_tiao_jian,
            u'是否推荐': self.shi_fou_tui_jian,
            u'类别': self.lei_bie,
            u'发布': self.fa_bu
        }