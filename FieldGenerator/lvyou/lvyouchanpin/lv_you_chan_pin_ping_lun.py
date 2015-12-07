# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class lv_you_chan_pin_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.sheng_fen = None
        self.jing_dian = None
        self.chan_pin_lei_xing = None
        self.lv_you_fang_shi = None
        self.chan_pin_te_se = None
        self.chu_fa_di = None
        self.mu_di_di = None
        self.chu_xing_fang_shi = None
        self.chan_pin_ming_cheng = None
        self.chan_pin_xing_ji = None
        self.yong_hu_ming = None
        self.hui_yuan_deng_ji = None
        self.jia_ge = None
        self.zong_ping_fen = None
        self.ping_lun_shi_jian = None
        self.ping_lun_lei_xing = None
        self.ping_lun_shu_liang = None
        self.ping_lun_nei_rong = None
        self.fen_shu = None
        self.dian_zan_shu_liang = None
        self.yu_ding_guo_cheng = None
        self.yu_ding_you_hui = None
        self.qu_piao_bian_jie = None
        self.jing_dian_ping_fen = None
        self.jiu_dian_ping_fen = None
        self.fu_wu_ping_fen = None
        self.jiao_tong_ping_fen = None
        self.ke_hu_man_yi_du = None
        self.fei_chang_man_yi = None
        self.bi_jiao_man_yi = None
        self.ji_ben_man_yi = None
        self.bu_man_yi = None
        self.fei_chang_bu_man_yi = None
        self.song_ji_fen = None
        self.lei_ji_yu_ding = None
        self.chu_fa_ri_qi = None
        self.chu_fa_yue_fen = None
        self.jing_qu_fu_wu = None
        self.di_qu = None
        self.xing_cheng_an_pai = None
        self.hao_ping_lv = None
        self.xing_cheng_tian_shu = None
        self.hui_da_zong_shu = None
        self.xiao_shou_dian_pu = None
        self.shang_pin_bao_han = None
        self.chu_you_ren_qun = None
        self.te_mai_lei_xing = None
        self.cheng_shi = None
        self.cheng_jiao_shi_jian = None
        self.chan_pin_bian_hao = None
        self.you_wan_jing_dian = None
        self.ru_zhu_jiu_dian = None
        self.yong_hu_tui_jian_lv = None
        self.jing_qu_dian_ping_shu = None
        self.jiu_dian_dian_ping_shu = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.you_tu_zong_shu = None
        self.chu_you_lei_xing = None
        self.you_wan_shi_jian = None
        self.dao_you_fu_wu = None
        self.jiao_tong = None
        self.can_yin_zhu_su = None
        self.tong_cheng_fu_wu = None
        self.you_yong_shu_liang = None
        self.ping_lun_lai_yuan = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'省份': self.sheng_fen,
            u'景点': self.jing_dian,
            u'产品类型': self.chan_pin_lei_xing,
            u'旅游方式': self.lv_you_fang_shi,
            u'产品特色': self.chan_pin_te_se,
            u'出发地': self.chu_fa_di,
            u'目的地': self.mu_di_di,
            u'出行方式': self.chu_xing_fang_shi,
            u'产品名称': self.chan_pin_ming_cheng,
            u'产品星级': self.chan_pin_xing_ji,
            u'用户名': self.yong_hu_ming,
            u'会员等级': self.hui_yuan_deng_ji,
            u'价格': self.jia_ge,
            u'总评分': self.zong_ping_fen,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论类型': self.ping_lun_lei_xing,
            u'评论数量': self.ping_lun_shu_liang,
            u'评论内容': self.ping_lun_nei_rong,
            u'分数': self.fen_shu,
            u'点赞数量': self.dian_zan_shu_liang,
            u'预订过程': self.yu_ding_guo_cheng,
            u'预定优惠': self.yu_ding_you_hui,
            u'取票便捷': self.qu_piao_bian_jie,
            u'景点评分': self.jing_dian_ping_fen,
            u'酒店评分': self.jiu_dian_ping_fen,
            u'服务评分': self.fu_wu_ping_fen,
            u'交通评分': self.jiao_tong_ping_fen,
            u'客户满意度': self.ke_hu_man_yi_du,
            u'非常满意': self.fei_chang_man_yi,
            u'比较满意': self.bi_jiao_man_yi,
            u'基本满意': self.ji_ben_man_yi,
            u'不满意': self.bu_man_yi,
            u'非常不满意': self.fei_chang_bu_man_yi,
            u'送积分': self.song_ji_fen,
            u'累计预订': self.lei_ji_yu_ding,
            u'出发日期': self.chu_fa_ri_qi,
            u'出发月份': self.chu_fa_yue_fen,
            u'景区服务': self.jing_qu_fu_wu,
            u'地区': self.di_qu,
            u'行程安排': self.xing_cheng_an_pai,
            u'好评率': self.hao_ping_lv,
            u'行程天数': self.xing_cheng_tian_shu,
            u'回答总数': self.hui_da_zong_shu,
            u'销售店铺': self.xiao_shou_dian_pu,
            u'商品包含': self.shang_pin_bao_han,
            u'出游人群': self.chu_you_ren_qun,
            u'特卖类型': self.te_mai_lei_xing,
            u'城市': self.cheng_shi,
            u'成交时间': self.cheng_jiao_shi_jian,
            u'产品编号': self.chan_pin_bian_hao,
            u'游玩景点': self.you_wan_jing_dian,
            u'入住酒店': self.ru_zhu_jiu_dian,
            u'用户推荐率': self.yong_hu_tui_jian_lv,
            u'景区点评数': self.jing_qu_dian_ping_shu,
            u'酒店点评数': self.jiu_dian_dian_ping_shu,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'有图总数': self.you_tu_zong_shu,
            u'出游类型': self.chu_you_lei_xing,
            u'游玩时间': self.you_wan_shi_jian,
            u'导游服务': self.dao_you_fu_wu,
            u'交通': self.jiao_tong,
            u'餐饮住宿': self.can_yin_zhu_su,
            u'同城服务': self.tong_cheng_fu_wu,
            u'有用数量': self.you_yong_shu_liang,
            u'评论来源': self.ping_lun_lai_yuan
        }