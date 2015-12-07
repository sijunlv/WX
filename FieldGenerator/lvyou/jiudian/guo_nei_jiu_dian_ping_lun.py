# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_jiu_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.jiu_dian_ming_cheng = None
        self.jiu_dian_pai_ming = None
        self.ping_lun_zong_shu = None
        self.xiang_xi_di_zhi = None
        self.yong_hu_ming = None
        self.zong_he_ping_fen = None
        self.ping_lun_nei_rong = None
        self.ping_lun_shi_jian = None
        self.qu_yu = None
        self.ru_zhu_shi_jian = None
        self.hao_ping_shu = None
        self.zhong_ping_shu = None
        self.cha_ping_shu = None
        self.lian_suo_pin_pai = None
        self.jiu_dian_lei_xing = None
        self.fang_xing = None
        self.zhui_jia_ping_lun_zong_shu = None
        self.wei_sheng_ping_fen = None
        self.she_shi_ping_fen = None
        self.fu_wu_ping_fen = None
        self.xing_jia_bi_ping_fen = None
        self.wen_da_zong_shu = None
        self.gong_lve_ti_ji_shu_liang = None
        self.hui_yuan_jue_se = None
        self.hui_yuan_deng_ji = None
        self.zhuan_jia_dian_ping_shu = None
        self.zu_ji_shu_liang = None
        self.ping_lun_guan_jian_ci = None
        self.ping_lun_lai_yuan = None
        self.you_yong_shu_liang = None
        self.ru_zhu_lei_xing = None
        self.yong_hu_man_yi_du = None
        self.jiao_tong = None
        self.she_shi = None
        self.wei_sheng_fu_wu = None
        self.tui_jian_lei_xing = None
        self.tui_jian_lv = None
        self.fu_wu_shui_ping = None
        self.shou_cang_shu_liang = None
        self.yong_hu_deng_ji = None
        self.chu_you_ren_qun = None
        self.xiang_mu = None
        self.can_yin = None
        self.hua_suan = None
        self.gong_xian_zhi = None
        self.ting_che_xin_xi = None
        self.ren_jun = None
        self.you_yong_fen = None
        self.wu_yong_fen = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'酒店名称': self.jiu_dian_ming_cheng,
            u'酒店排名': self.jiu_dian_pai_ming,
            u'评论总数': self.ping_lun_zong_shu,
            u'详细地址': self.xiang_xi_di_zhi,
            u'用户名': self.yong_hu_ming,
            u'综合评分': self.zong_he_ping_fen,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论时间': self.ping_lun_shi_jian,
            u'区域': self.qu_yu,
            u'入住时间': self.ru_zhu_shi_jian,
            u'好评数': self.hao_ping_shu,
            u'中评数': self.zhong_ping_shu,
            u'差评数': self.cha_ping_shu,
            u'连锁品牌': self.lian_suo_pin_pai,
            u'酒店类型': self.jiu_dian_lei_xing,
            u'房型': self.fang_xing,
            u'追加评论总数': self.zhui_jia_ping_lun_zong_shu,
            u'卫生评分': self.wei_sheng_ping_fen,
            u'设施评分': self.she_shi_ping_fen,
            u'服务评分': self.fu_wu_ping_fen,
            u'性价比评分': self.xing_jia_bi_ping_fen,
            u'问答总数': self.wen_da_zong_shu,
            u'攻略提及数量': self.gong_lve_ti_ji_shu_liang,
            u'会员角色': self.hui_yuan_jue_se,
            u'会员等级': self.hui_yuan_deng_ji,
            u'砖家点评数': self.zhuan_jia_dian_ping_shu,
            u'足迹数量': self.zu_ji_shu_liang,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'评论来源': self.ping_lun_lai_yuan,
            u'有用数量': self.you_yong_shu_liang,
            u'入住类型': self.ru_zhu_lei_xing,
            u'用户满意度': self.yong_hu_man_yi_du,
            u'交通': self.jiao_tong,
            u'设施': self.she_shi,
            u'卫生服务': self.wei_sheng_fu_wu,
            u'推荐类型': self.tui_jian_lei_xing,
            u'推荐率': self.tui_jian_lv,
            u'服务水平': self.fu_wu_shui_ping,
            u'收藏数量': self.shou_cang_shu_liang,
            u'用户等级': self.yong_hu_deng_ji,
            u'出游人群': self.chu_you_ren_qun,
            u'项目': self.xiang_mu,
            u'餐饮': self.can_yin,
            u'划算': self.hua_suan,
            u'贡献值': self.gong_xian_zhi,
            u'停车信息': self.ting_che_xin_xi,
            u'人均': self.ren_jun,
            u'有用分': self.you_yong_fen,
            u'无用分': self.wu_yong_fen
        }