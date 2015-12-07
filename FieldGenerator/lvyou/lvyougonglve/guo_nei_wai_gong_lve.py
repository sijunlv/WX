# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_wai_gong_lve(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.guo_jia = None
        self.qu_yu = None
        self.di_qu = None
        self.cheng_shi = None
        self.chu_fa_di = None
        self.gong_lve_shu_liang = None
        self.gong_lve_lei_xing = None
        self.dian_ping_shu = None
        self.biao_qian = None
        self.you_wan_di_dian = None
        self.you_ji = None
        self.you_ji_biao_ti = None
        self.you_ji_zuo_zhe = None
        self.deng_ji = None
        self.you_ji_nei_rong = None
        self.fa_biao_shi_jian = None
        self.liu_lan_liang = None
        self.xia_zai_liang = None
        self.dian_zan_liang = None
        self.hui_fu_shu = None
        self.yong_hu_ming = None
        self.xing_bie = None
        self.tu_jing_jing_dian = None
        self.ren_jun_kai_xiao = None
        self.xing_cheng_tian_shu = None
        self.chu_fa_ri_qi = None
        self.dao_da_ri_qi = None
        self.xi_huan_ren_shu = None
        self.qu_guo_ren_shu = None
        self.you_ji_shu_liang = None
        self.jing_dian_shu_liang = None

    def makemap(self):
        return {
            u'国家': self.guo_jia,
            u'区域': self.qu_yu,
            u'地区': self.di_qu,
            u'城市': self.cheng_shi,
            u'出发地': self.chu_fa_di,
            u'攻略数量': self.gong_lve_shu_liang,
            u'攻略类型': self.gong_lve_lei_xing,
            u'点评数': self.dian_ping_shu,
            u'标签': self.biao_qian,
            u'游玩地点': self.you_wan_di_dian,
            u'游记': self.you_ji,
            u'游记标题': self.you_ji_biao_ti,
            u'游记作者': self.you_ji_zuo_zhe,
            u'等级': self.deng_ji,
            u'游记内容': self.you_ji_nei_rong,
            u'发表时间': self.fa_biao_shi_jian,
            u'浏览量': self.liu_lan_liang,
            u'下载量': self.xia_zai_liang,
            u'点赞量': self.dian_zan_liang,
            u'回复数': self.hui_fu_shu,
            u'用户名': self.yong_hu_ming,
            u'性别': self.xing_bie,
            u'途径景点': self.tu_jing_jing_dian,
            u'人均开销': self.ren_jun_kai_xiao,
            u'行程天数': self.xing_cheng_tian_shu,
            u'出发日期': self.chu_fa_ri_qi,
            u'到达日期': self.dao_da_ri_qi,
            u'喜欢人数': self.xi_huan_ren_shu,
            u'去过人数': self.qu_guo_ren_shu,
            u'游记数量': self.you_ji_shu_liang,
            u'景点数量': self.jing_dian_shu_liang
        }