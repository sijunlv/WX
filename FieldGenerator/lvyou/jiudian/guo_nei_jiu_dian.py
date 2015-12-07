# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_jiu_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.jiu_dian_ming_cheng = None
        self.jiu_dian_pai_ming = None
        self.jiu_dian_ji_bie = None
        self.ping_lun_zong_shu = None
        self.xiang_xi_di_zhi = None
        self.jia_ge = None
        self.qu_yu = None
        self.xiao_liang = None
        self.ru_zhu_shi_jian = None
        self.hao_ping_shu = None
        self.cha_ping_shu = None
        self.lian_suo_pin_pai = None
        self.shang_ye_quan = None
        self.jiu_dian_lei_xing = None
        self.zong_he_ping_jia = None
        self.li_dian_shi_jian = None
        self.fang_xing = None
        self.chuang_xing = None
        self.shang_wang_fang_shi = None
        self.mian_ji = None
        self.liu_ceng = None
        self.chuang_xing_1 = None
        self.mai_jia = None
        self.chu_li_shi_chang = None
        self.yu_ding_cheng_gong_lv = None
        self.yu_ding_xiang_qing = None
        self.xing_jia_bi_ping_fen = None
        self.fang_xing_1 = None
        self.fang_xing_2 = None
        self.zao_can = None
        self.zheng_ce = None
        self.jiao_tong = None
        self.she_shi = None
        self.wei_sheng_fu_wu = None
        self.tui_jian_lei_xing = None
        self.tui_jian_lv = None
        self.fu_wu_shui_ping = None
        self.shou_cang_shu_liang = None
        self.you_xiao_qi = None
        self.can_yin_ping_fen = None
        self.wei_yu_ping_fen = None
        self.shui_mian_huan_jing = None
        self.wang_luo_huan_jing = None
        self.ke_fang_ping_fen = None
        self.shu_shi_di_fen = None
        self.qu_xiao_zheng_ce = None
        self.fan_qian_ri_jun_jia = None
        self.zhi_fu_fang_shi = None
        self.qi_jia = None
        self.fang_yuan = None
        self.sheng_yu_liang = None
        self.you_hui = None
        self.hui_yuan_zhe_kou = None
        self.bao_jia_lai_yuan = None
        self.ping_fen_lai_yuan = None
        self.guo_jia = None
        self.sheng_fen = None
        self.biao_qian = None
        self.you_ji_ti_ji_shu_liang = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'酒店名称': self.jiu_dian_ming_cheng,
            u'酒店排名': self.jiu_dian_pai_ming,
            u'酒店级别': self.jiu_dian_ji_bie,
            u'评论总数': self.ping_lun_zong_shu,
            u'详细地址': self.xiang_xi_di_zhi,
            u'价格': self.jia_ge,
            u'区域': self.qu_yu,
            u'销量': self.xiao_liang,
            u'入住时间': self.ru_zhu_shi_jian,
            u'好评数': self.hao_ping_shu,
            u'差评数': self.cha_ping_shu,
            u'连锁品牌': self.lian_suo_pin_pai,
            u'商业圈': self.shang_ye_quan,
            u'酒店类型': self.jiu_dian_lei_xing,
            u'综合评价': self.zong_he_ping_jia,
            u'离店时间': self.li_dian_shi_jian,
            u'房型': self.fang_xing,
            u'床型': self.chuang_xing,
            u'上网方式': self.shang_wang_fang_shi,
            u'面积': self.mian_ji,
            u'六层': self.liu_ceng,
            u'窗型1': self.chuang_xing_1,
            u'卖家': self.mai_jia,
            u'处理时长': self.chu_li_shi_chang,
            u'预定成功率': self.yu_ding_cheng_gong_lv,
            u'预订详情': self.yu_ding_xiang_qing,
            u'性价比评分': self.xing_jia_bi_ping_fen,
            u'房型1': self.fang_xing_1,
            u'房型2': self.fang_xing_2,
            u'早餐': self.zao_can,
            u'政策': self.zheng_ce,
            u'交通': self.jiao_tong,
            u'设施': self.she_shi,
            u'卫生服务': self.wei_sheng_fu_wu,
            u'推荐类型': self.tui_jian_lei_xing,
            u'推荐率': self.tui_jian_lv,
            u'服务水平': self.fu_wu_shui_ping,
            u'收藏数量': self.shou_cang_shu_liang,
            u'有效期': self.you_xiao_qi,
            u'餐饮评分': self.can_yin_ping_fen,
            u'卫浴评分': self.wei_yu_ping_fen,
            u'睡眠环境': self.shui_mian_huan_jing,
            u'网络环境': self.wang_luo_huan_jing,
            u'客房评分': self.ke_fang_ping_fen,
            u'舒适的分': self.shu_shi_di_fen,
            u'取消政策': self.qu_xiao_zheng_ce,
            u'返前日均价': self.fan_qian_ri_jun_jia,
            u'支付方式': self.zhi_fu_fang_shi,
            u'起价': self.qi_jia,
            u'房源': self.fang_yuan,
            u'剩余量': self.sheng_yu_liang,
            u'优惠': self.you_hui,
            u'会员折扣': self.hui_yuan_zhe_kou,
            u'报价来源': self.bao_jia_lai_yuan,
            u'评分来源': self.ping_fen_lai_yuan,
            u'国家': self.guo_jia,
            u'省份': self.sheng_fen,
            u'标签': self.biao_qian,
            u'游记提及数量': self.you_ji_ti_ji_shu_liang
        }