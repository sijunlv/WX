# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class you_lun_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.you_lun_hang_xian = None
        self.chan_pin_ming_cheng = None
        self.chan_pin_bian_hao = None
        self.you_lun_gong_si = None
        self.shang_chuan_di_dian = None
        self.xia_chuan_di_dian = None
        self.you_lun_chuan_dui = None
        self.dang_qian_chuan_qi = None
        self.wen_xin_ti_shi = None
        self.hao_ping_lv = None
        self.zhong_ping_lv = None
        self.cha_ping_lv = None
        self.zong_he_ping_fen = None
        self.you_lun_fu_wu = None
        self.you_lun_zhu_su = None
        self.can_yin_zhu_su = None
        self.yu_le_huo_dong = None
        self.an_shang_guan_guang = None
        self.dian_ping_zong_shu = None
        self.man_yi_du = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.you_tu_ping_lun_zong_shu = None
        self.yong_hu_ming = None
        self.hui_yuan_deng_ji = None
        self.ping_lun_nei_rong = None
        self.chu_you_fang_shi = None
        self.ping_lun_shi_jian = None
        self.ping_lun_lai_yuan = None
        self.wang_fan_jiao_tong = None
        self.yu_ding_guo_cheng = None
        self.xing_cheng_an_pai = None
        self.dian_zan_liang = None
        self.hui_fu_liang = None
        self.fan_huan = None
        self.song_ji_fen = None
        self.ke_fu = None
        self.fen_shu = None

    def makemap(self):
        return {
            u'邮轮航线': self.you_lun_hang_xian,
            u'产品名称': self.chan_pin_ming_cheng,
            u'产品编号': self.chan_pin_bian_hao,
            u'邮轮公司': self.you_lun_gong_si,
            u'上船地点': self.shang_chuan_di_dian,
            u'下船地点': self.xia_chuan_di_dian,
            u'邮轮船队': self.you_lun_chuan_dui,
            u'当前船期': self.dang_qian_chuan_qi,
            u'温馨提示': self.wen_xin_ti_shi,
            u'好评率': self.hao_ping_lv,
            u'中评率': self.zhong_ping_lv,
            u'差评率': self.cha_ping_lv,
            u'综合评分': self.zong_he_ping_fen,
            u'游轮服务': self.you_lun_fu_wu,
            u'游轮住宿': self.you_lun_zhu_su,
            u'餐饮住宿': self.can_yin_zhu_su,
            u'娱乐活动': self.yu_le_huo_dong,
            u'岸上观光': self.an_shang_guan_guang,
            u'点评总数': self.dian_ping_zong_shu,
            u'满意度': self.man_yi_du,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'有图评论总数': self.you_tu_ping_lun_zong_shu,
            u'用户名': self.yong_hu_ming,
            u'会员等级': self.hui_yuan_deng_ji,
            u'评论内容': self.ping_lun_nei_rong,
            u'出游方式': self.chu_you_fang_shi,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论来源': self.ping_lun_lai_yuan,
            u'往返交通': self.wang_fan_jiao_tong,
            u'预订过程': self.yu_ding_guo_cheng,
            u'行程安排': self.xing_cheng_an_pai,
            u'点赞量': self.dian_zan_liang,
            u'回复量': self.hui_fu_liang,
            u'返还': self.fan_huan,
            u'送积分': self.song_ji_fen,
            u'客服': self.ke_fu,
            u'分数': self.fen_shu
        }