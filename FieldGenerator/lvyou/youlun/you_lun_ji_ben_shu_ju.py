# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class you_lun_ji_ben_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.you_lun_pin_pai = None
        self.you_lun_hang_xian = None
        self.chan_pin_ming_cheng = None
        self.chan_pin_bian_hao = None
        self.biao_qian = None
        self.chu_hang_ri_qi = None
        self.ti_qian_yu_ding = None
        self.xing_cheng_tian_shu = None
        self.you_hui_xin_xi = None
        self.you_lun_gong_si = None
        self.shang_chuan_di_dian = None
        self.xia_chuan_di_dian = None
        self.tu_jing_gang_kou = None
        self.jia_ge = None
        self.xiao_liang = None
        self.xiao_shou_dian_pu = None
        self.you_lun_chuan_dui = None
        self.dang_qian_chuan_qi = None
        self.wen_xin_ti_shi = None
        self.hao_ping_lv = None
        self.zong_he_ping_fen = None
        self.dian_ping_zong_shu = None
        self.guan_zhu_zong_shu = None
        self.man_yi_du = None
        self.fan_hui_di = None
        self.chu_fa_lu_xian = None
        self.qian_zheng_cai_liao = None
        self.you_lun_xing_hao = None
        self.can_yu_ren_shu = None
        self.wang_fan_jiao_tong = None
        self.xing_cheng_zong_fen = None
        self.jiao_tong_zong_fen = None
        self.shi_su_zong_fen = None
        self.fu_wu_zong_fen = None
        self.song_ji_fen = None
        self.zi_xun_nei_rong = None
        self.you_zai_ke_fu = None
        self.zi_xun_shi_jian = None
        self.fei_chang_man_yi = None
        self.bi_jiao_man_yi = None
        self.ji_ben_man_yi = None
        self.bu_man_yi = None
        self.fei_chang_bu_man_yi = None

    def makemap(self):
        return {
            u'邮轮品牌': self.you_lun_pin_pai,
            u'邮轮航线': self.you_lun_hang_xian,
            u'产品名称': self.chan_pin_ming_cheng,
            u'产品编号': self.chan_pin_bian_hao,
            u'标签': self.biao_qian,
            u'出航日期': self.chu_hang_ri_qi,
            u'提前预定': self.ti_qian_yu_ding,
            u'行程天数': self.xing_cheng_tian_shu,
            u'优惠信息': self.you_hui_xin_xi,
            u'邮轮公司': self.you_lun_gong_si,
            u'上船地点': self.shang_chuan_di_dian,
            u'下船地点': self.xia_chuan_di_dian,
            u'途径港口': self.tu_jing_gang_kou,
            u'价格': self.jia_ge,
            u'销量': self.xiao_liang,
            u'销售店铺': self.xiao_shou_dian_pu,
            u'邮轮船队': self.you_lun_chuan_dui,
            u'当前船期': self.dang_qian_chuan_qi,
            u'温馨提示': self.wen_xin_ti_shi,
            u'好评率': self.hao_ping_lv,
            u'综合评分': self.zong_he_ping_fen,
            u'点评总数': self.dian_ping_zong_shu,
            u'关注总数': self.guan_zhu_zong_shu,
            u'满意度': self.man_yi_du,
            u'返回地': self.fan_hui_di,
            u'出发路线': self.chu_fa_lu_xian,
            u'签证材料': self.qian_zheng_cai_liao,
            u'邮轮型号': self.you_lun_xing_hao,
            u'参与人数': self.can_yu_ren_shu,
            u'往返交通': self.wang_fan_jiao_tong,
            u'行程总分': self.xing_cheng_zong_fen,
            u'交通总分': self.jiao_tong_zong_fen,
            u'食宿总分': self.shi_su_zong_fen,
            u'服务总分': self.fu_wu_zong_fen,
            u'送积分': self.song_ji_fen,
            u'咨询内容': self.zi_xun_nei_rong,
            u'悠哉客服': self.you_zai_ke_fu,
            u'咨询时间': self.zi_xun_shi_jian,
            u'非常满意': self.fei_chang_man_yi,
            u'比较满意': self.bi_jiao_man_yi,
            u'基本满意': self.ji_ben_man_yi,
            u'不满意': self.bu_man_yi,
            u'非常不满意': self.fei_chang_bu_man_yi
        }