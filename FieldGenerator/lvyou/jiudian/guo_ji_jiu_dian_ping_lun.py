# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_ji_jiu_dian_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.jiu_dian_ming = None
        self.yong_hu_ming = None
        self.xing_jia_bi_ping_fen = None
        self.ping_lun_nei_rong = None
        self.ping_lun_shi_jian = None
        self.qu_yu = None
        self.zong_he_ping_fen = None
        self.ru_zhu_shi_jian = None
        self.fang_xing = None
        self.hao_ping_shu = None
        self.zhong_ping_shu = None
        self.cha_ping_zong_shu = None
        self.zhui_jia_ping_lun_shu = None
        self.jiu_dian_lei_xing = None
        self.yu_ding_wang_zhan = None
        self.wen_da_zong_shu = None
        self.gong_lve_ti_ji_shu_liang = None
        self.di_li_wei_zhi = None
        self.huan_jing_wei_sheng = None
        self.can_yin_fu_wu = None
        self.fu_wu_zhi_liang = None
        self.she_shi = None
        self.hui_yuan_jue_se = None
        self.hui_yuan_deng_ji = None
        self.zhuan_jia_dian_ping_shu_liang = None
        self.zu_ji_shu_liang = None
        self.ping_lun_guan_jian_ci = None
        self.ru_zhu_lei_xing = None
        self.ping_lun_lai_yuan = None
        self.you_yong_shu_liang = None
        self.guo_jia = None
        self.yong_hu_tui_jian_lv = None
        self.jiu_dian_pin_pai = None
        self.you_ji_dian_ping_zong_shu = None
        self.zhu_su_mu_di = None
        self.you_dian = None
        self.bu_zu = None
        self.ping_jia = None
        self.zong_ping_jia = None
        self.ping_jia_yuan = None
        self.chu_xian_tiao_shu = None
        self.ken_ding_nei_rong = None
        self.fou_ding_nei_rong = None
        self.shu_shi_du = None
        self.ping_lun_zong_shu = None
        self.gong_xian_zhi = None
        self.ren_jun = None
        self.xiang_mu = None
        self.can_yin = None
        self.hua_suan = None
        self.ting_che_xin_xi = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'酒店名': self.jiu_dian_ming,
            u'用户名': self.yong_hu_ming,
            u'性价比评分': self.xing_jia_bi_ping_fen,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论时间': self.ping_lun_shi_jian,
            u'区域': self.qu_yu,
            u'综合评分': self.zong_he_ping_fen,
            u'入住时间': self.ru_zhu_shi_jian,
            u'房型': self.fang_xing,
            u'好评数': self.hao_ping_shu,
            u'中评数': self.zhong_ping_shu,
            u'差评总数': self.cha_ping_zong_shu,
            u'追加评论数': self.zhui_jia_ping_lun_shu,
            u'酒店类型': self.jiu_dian_lei_xing,
            u'预订网站': self.yu_ding_wang_zhan,
            u'问答总数': self.wen_da_zong_shu,
            u'攻略提及数量': self.gong_lve_ti_ji_shu_liang,
            u'地理位置': self.di_li_wei_zhi,
            u'环境卫生': self.huan_jing_wei_sheng,
            u'餐饮服务': self.can_yin_fu_wu,
            u'服务质量': self.fu_wu_zhi_liang,
            u'设施': self.she_shi,
            u'会员角色': self.hui_yuan_jue_se,
            u'会员等级': self.hui_yuan_deng_ji,
            u'砖家点评数量': self.zhuan_jia_dian_ping_shu_liang,
            u'足迹数量': self.zu_ji_shu_liang,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'入住类型': self.ru_zhu_lei_xing,
            u'评论来源': self.ping_lun_lai_yuan,
            u'有用数量': self.you_yong_shu_liang,
            u'国家': self.guo_jia,
            u'用户推荐率': self.yong_hu_tui_jian_lv,
            u'酒店品牌': self.jiu_dian_pin_pai,
            u'游记点评总数': self.you_ji_dian_ping_zong_shu,
            u'住宿目的': self.zhu_su_mu_di,
            u'优点': self.you_dian,
            u'不足': self.bu_zu,
            u'评价': self.ping_jia,
            u'总评价': self.zong_ping_jia,
            u'评价源': self.ping_jia_yuan,
            u'出现条数': self.chu_xian_tiao_shu,
            u'肯定内容': self.ken_ding_nei_rong,
            u'否定内容': self.fou_ding_nei_rong,
            u'舒适度': self.shu_shi_du,
            u'评论总数': self.ping_lun_zong_shu,
            u'贡献值': self.gong_xian_zhi,
            u'人均': self.ren_jun,
            u'项目': self.xiang_mu,
            u'餐饮': self.can_yin,
            u'划算': self.hua_suan,
            u'停车信息': self.ting_che_xin_xi
        }