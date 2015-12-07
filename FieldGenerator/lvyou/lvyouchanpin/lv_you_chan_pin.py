# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class lv_you_chan_pin(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.sheng_fen = None
        self.jing_dian_wei_zhi_1 = None
        self.jing_dian_wei_zhi_2 = None
        self.jing_dian = None
        self.chan_pin_lei_xing = None
        self.biao_qian = None
        self.biao_qian_2 = None
        self.lv_you_fang_shi = None
        self.chan_pin_te_se = None
        self.chan_pin_te_dian = None
        self.kai_qiang_shi_jian = None
        self.chu_fa_di = None
        self.mu_di_di = None
        self.chu_xing_fang_shi = None
        self.chan_pin_ming_cheng = None
        self.chan_pin_xing_ji = None
        self.jia_ge = None
        self.zong_ping_fen = None
        self.ping_lun_lei_xing = None
        self.ping_lun_shu_liang = None
        self.ping_lun_nei_rong = None
        self.yu_ding_you_hui = None
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
        self.er_tong_jia = None
        self.dan_fang_cha = None
        self.ke_xuan_hang_xian_shu_liang = None
        self.ke_xuan_jiu_dian_shu_liang = None
        self.cheng_ren_jia = None
        self.you_lun_gong_si = None
        self.lei_ji_yu_ding = None
        self.chu_fa_ri_qi = None
        self.di_qu = None
        self.xing_cheng_an_pai = None
        self.xiao_liang = None
        self.tu_jing_cheng_shi = None
        self.hao_ping_lv = None
        self.yu_liang = None
        self.xiang_qu_ren_shu = None
        self.qu_guo_ren_shu = None
        self.lv_you_gong_lve_xia_zai_liang = None
        self.you_ji_shu_liang = None
        self.liu_lan_ren_shu = None
        self.xing_cheng_tian_shu = None
        self.guan_zhu_ren_shu = None
        self.nv_xing_ren_shu = None
        self.nan_xing_ren_shu = None
        self.pai_ming = None
        self.hui_da_zong_shu = None
        self.yong_hu_zhuang_tai = None
        self.wang_fan_jiao_tong = None
        self.chan_pin_sheng_yu_liang = None
        self.fu_kuan_fang_shi = None
        self.fu_kuan_shi_jian = None
        self.xiao_shou_dian_pu = None
        self.shang_pin_bao_han = None
        self.chu_you_ren_qun = None
        self.te_mai_lei_xing = None
        self.cheng_shi = None
        self.chan_pin_bian_hao = None
        self.you_wan_jing_dian = None
        self.ru_zhu_jiu_dian = None
        self.hao_ping_zong_shu = None
        self.zhong_ping_zong_shu = None
        self.cha_ping_zong_shu = None
        self.you_tu_zong_shu = None
        self.chu_you_lei_xing = None
        self.tong_cheng_fu_wu = None
        self.qiang_gou_lv = None
        self.nei_rong_jie_shao = None
        self.yong_hu_ming = None
        self.deng_ji = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'省份': self.sheng_fen,
            u'景点位置1': self.jing_dian_wei_zhi_1,
            u'景点位置2': self.jing_dian_wei_zhi_2,
            u'景点': self.jing_dian,
            u'产品类型': self.chan_pin_lei_xing,
            u'标签': self.biao_qian,
            u'标签2': self.biao_qian_2,
            u'旅游方式': self.lv_you_fang_shi,
            u'产品特色': self.chan_pin_te_se,
            u'产品特点': self.chan_pin_te_dian,
            u'开抢时间': self.kai_qiang_shi_jian,
            u'出发地': self.chu_fa_di,
            u'目的地': self.mu_di_di,
            u'出行方式': self.chu_xing_fang_shi,
            u'产品名称': self.chan_pin_ming_cheng,
            u'产品星级': self.chan_pin_xing_ji,
            u'价格': self.jia_ge,
            u'总评分': self.zong_ping_fen,
            u'评论类型': self.ping_lun_lei_xing,
            u'评论数量': self.ping_lun_shu_liang,
            u'评论内容': self.ping_lun_nei_rong,
            u'预定优惠': self.yu_ding_you_hui,
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
            u'儿童价': self.er_tong_jia,
            u'单房差': self.dan_fang_cha,
            u'可选航线数量': self.ke_xuan_hang_xian_shu_liang,
            u'可选酒店数量': self.ke_xuan_jiu_dian_shu_liang,
            u'成人价': self.cheng_ren_jia,
            u'邮轮公司': self.you_lun_gong_si,
            u'累计预订': self.lei_ji_yu_ding,
            u'出发日期': self.chu_fa_ri_qi,
            u'地区': self.di_qu,
            u'行程安排': self.xing_cheng_an_pai,
            u'销量': self.xiao_liang,
            u'途经城市': self.tu_jing_cheng_shi,
            u'好评率': self.hao_ping_lv,
            u'余量': self.yu_liang,
            u'想去人数': self.xiang_qu_ren_shu,
            u'去过人数': self.qu_guo_ren_shu,
            u'旅游功略下载量': self.lv_you_gong_lve_xia_zai_liang,
            u'游记数量': self.you_ji_shu_liang,
            u'浏览人数': self.liu_lan_ren_shu,
            u'行程天数': self.xing_cheng_tian_shu,
            u'关注人数': self.guan_zhu_ren_shu,
            u'女性人数': self.nv_xing_ren_shu,
            u'男性人数': self.nan_xing_ren_shu,
            u'排名': self.pai_ming,
            u'回答总数': self.hui_da_zong_shu,
            u'用户状态': self.yong_hu_zhuang_tai,
            u'往返交通': self.wang_fan_jiao_tong,
            u'产品剩余量': self.chan_pin_sheng_yu_liang,
            u'付款方式': self.fu_kuan_fang_shi,
            u'付款时间': self.fu_kuan_shi_jian,
            u'销售店铺': self.xiao_shou_dian_pu,
            u'商品包含': self.shang_pin_bao_han,
            u'出游人群': self.chu_you_ren_qun,
            u'特卖类型': self.te_mai_lei_xing,
            u'城市': self.cheng_shi,
            u'产品编号': self.chan_pin_bian_hao,
            u'游玩景点': self.you_wan_jing_dian,
            u'入住酒店': self.ru_zhu_jiu_dian,
            u'好评总数': self.hao_ping_zong_shu,
            u'中评总数': self.zhong_ping_zong_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'有图总数': self.you_tu_zong_shu,
            u'出游类型': self.chu_you_lei_xing,
            u'同城服务': self.tong_cheng_fu_wu,
            u'抢购率': self.qiang_gou_lv,
            u'内容介绍': self.nei_rong_jie_shao,
            u'用户名': self.yong_hu_ming,
            u'等级': self.deng_ji
        }