# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_ji_jiu_dian(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.jiu_dian_ming = None
        self.jiu_dian_pai_ming = None
        self.xing_ji = None
        self.ping_lun_shu = None
        self.xiang_xi_di_zhi = None
        self.jia_ge = None
        self.xiang_mu = None
        self.can_yin = None
        self.xing_jia_bi_ping_fen = None
        self.ting_che_xin_xi = None
        self.qu_yu = None
        self.zong_he_ping_fen = None
        self.zong_he_ping_jia = None
        self.xiao_liang = None
        self.ru_zhu_shi_jian = None
        self.li_dian_shi_jian = None
        self.fang_xing = None
        self.chuang_xing = None
        self.shang_wang_fang_shi = None
        self.mian_ji = None
        self.lou_ceng = None
        self.chuang_xing_1 = None
        self.mai_jia = None
        self.chu_li_shi_chang = None
        self.yu_yue_cheng_gong_lv = None
        self.yu_ding_xiang_qing = None
        self.hao_ping_shu = None
        self.zhong_ping_shu = None
        self.cha_ping_zong_shu = None
        self.zhui_jia_ping_lun_shu = None
        self.jiu_dian_lei_xing = None
        self.ke_zhu_ren_shu = None
        self.wifi = None
        self.wei_yu = None
        self.yu_ding_wang_zhan = None
        self.zao_can = None
        self.kuan_dai = None
        self.di_li_wei_zhi = None
        self.huan_jing_wei_sheng = None
        self.fu_wu_zhi_liang = None
        self.she_shi = None
        self.zhao_pian_shu_liang = None
        self.hen_hao_shu_liang = None
        self.cha_shu_liang = None
        self.jia_ting_ping_lun = None
        self.fu_qi_ping_lun = None
        self.du_zi_lv_you_ping_lun = None
        self.shang_wu_ping_lun = None
        self.guo_jia = None
        self.di_qu = None
        self.yong_hu_tui_jian_lv = None
        self.shu_shi_du_ping_fen = None
        self.jiu_dian_pin_pai = None
        self.qu_xiao_zheng_ce = None
        self.ren_shu_shang_xian = None
        self.mei_jian_mei_wan_fang_jia = None
        self.jian_shu = None
        self.zong_ping_jia = None
        self.huan_jing_de_fen = None
        self.fu_wu_de_fen = None
        self.zao_can_fen = None
        self.fan_dian_fen = None
        self.shang_wu_lv_hang_shu = None
        self.lang_man_lv_xing_shu = None
        self.jia_ting_zhi_lv = None
        self.hao_you_jie_ban_shu = None
        self.qi_ta_lv_xing_shu = None
        self.wu_fen_shu_liang = None
        self.si_fen_shu_liang = None
        self.san_fen_shu_liang = None
        self.er_fen_shu_liang = None
        self.yi_fen_shu_liang = None
        self.tiao_jian_de_fen = None
        self.biao_qian = None
        self.you_ji_ti_ji_shu_liang = None
        self.ping_fen_lai_yuan = None
        self.zhi_fu_fang_shi = None
        self.bao_jia_lai_yuan = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'酒店名': self.jiu_dian_ming,
            u'酒店排名': self.jiu_dian_pai_ming,
            u'星级': self.xing_ji,
            u'评论数': self.ping_lun_shu,
            u'详细地址': self.xiang_xi_di_zhi,
            u'价格': self.jia_ge,
            u'项目': self.xiang_mu,
            u'餐饮': self.can_yin,
            u'性价比评分': self.xing_jia_bi_ping_fen,
            u'停车信息': self.ting_che_xin_xi,
            u'区域': self.qu_yu,
            u'综合评分': self.zong_he_ping_fen,
            u'综合评价': self.zong_he_ping_jia,
            u'销量': self.xiao_liang,
            u'入住时间': self.ru_zhu_shi_jian,
            u'离店时间': self.li_dian_shi_jian,
            u'房型': self.fang_xing,
            u'床型': self.chuang_xing,
            u'上网方式': self.shang_wang_fang_shi,
            u'面积': self.mian_ji,
            u'楼层': self.lou_ceng,
            u'窗型1': self.chuang_xing_1,
            u'卖家': self.mai_jia,
            u'处理时长': self.chu_li_shi_chang,
            u'预约成功率': self.yu_yue_cheng_gong_lv,
            u'预定详情': self.yu_ding_xiang_qing,
            u'好评数': self.hao_ping_shu,
            u'中评数': self.zhong_ping_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'追加评论数': self.zhui_jia_ping_lun_shu,
            u'酒店类型': self.jiu_dian_lei_xing,
            u'可住人数': self.ke_zhu_ren_shu,
            u'wifi': self.wifi,
            u'卫浴': self.wei_yu,
            u'预订网站': self.yu_ding_wang_zhan,
            u'早餐': self.zao_can,
            u'宽带': self.kuan_dai,
            u'地理位置': self.di_li_wei_zhi,
            u'环境卫生': self.huan_jing_wei_sheng,
            u'服务质量': self.fu_wu_zhi_liang,
            u'设施': self.she_shi,
            u'照片数量': self.zhao_pian_shu_liang,
            u'很好数量': self.hen_hao_shu_liang,
            u'差数量': self.cha_shu_liang,
            u'家庭评论': self.jia_ting_ping_lun,
            u'夫妻评论': self.fu_qi_ping_lun,
            u'独自旅游评论': self.du_zi_lv_you_ping_lun,
            u'商务评论': self.shang_wu_ping_lun,
            u'国家': self.guo_jia,
            u'地区': self.di_qu,
            u'用户推荐率': self.yong_hu_tui_jian_lv,
            u'舒适度评分': self.shu_shi_du_ping_fen,
            u'酒店品牌': self.jiu_dian_pin_pai,
            u'取消政策': self.qu_xiao_zheng_ce,
            u'人数上限': self.ren_shu_shang_xian,
            u'每间每晚放假': self.mei_jian_mei_wan_fang_jia,
            u'间数': self.jian_shu,
            u'总评价': self.zong_ping_jia,
            u'环境得分': self.huan_jing_de_fen,
            u'服务得分': self.fu_wu_de_fen,
            u'早餐分': self.zao_can_fen,
            u'饭店分': self.fan_dian_fen,
            u'商务旅行数': self.shang_wu_lv_hang_shu,
            u'浪漫旅行数': self.lang_man_lv_xing_shu,
            u'家庭之旅': self.jia_ting_zhi_lv,
            u'好友结伴数': self.hao_you_jie_ban_shu,
            u'其他旅行数': self.qi_ta_lv_xing_shu,
            u'5分数量': self.wu_fen_shu_liang,
            u'4分数量': self.si_fen_shu_liang,
            u'3分数量': self.san_fen_shu_liang,
            u'2分数量': self.er_fen_shu_liang,
            u'1分数量': self.yi_fen_shu_liang,
            u'条件得分': self.tiao_jian_de_fen,
            u'标签': self.biao_qian,
            u'游记提及数量': self.you_ji_ti_ji_shu_liang,
            u'评分来源': self.ping_fen_lai_yuan,
            u'支付方式': self.zhi_fu_fang_shi,
            u'报价来源': self.bao_jia_lai_yuan
        }