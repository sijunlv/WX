# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class men_piao_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.jing_dian_ming_cheng = None
        self.suo_shu_cheng_shi = None
        self.jing_qu_deng_ji = None
        self.you_ke_man_yi_du = None
        self.yong_hu_ming = None
        self.ping_lun_shi_jian = None
        self.ping_lun_nei_rong = None
        self.ping_lun_guan_jian_ci = None
        self.ping_lun_lei_xing = None
        self.chu_you_fang_shi = None
        self.dian_zan_shu_liang = None
        self.hui_fu_shu_liang = None
        self.cheng_ren_piao_jia_ge = None
        self.lao_ren_piao_jia_ge = None
        self.yu_ding_guo_cheng = None
        self.yu_ding_you_hui = None
        self.qu_piao_bian_jie = None
        self.jing_qu = None
        self.jing_qu_fu_wu = None
        self.xing_cheng = None
        self.dao_you = None
        self.jiao_tong = None
        self.zhu_su = None
        self.fan_huan = None
        self.song_ji_fen = None

    def makemap(self):
        return {
            u'景点名称': self.jing_dian_ming_cheng,
            u'所属城市': self.suo_shu_cheng_shi,
            u'景区等级': self.jing_qu_deng_ji,
            u'游客满意度': self.you_ke_man_yi_du,
            u'用户名': self.yong_hu_ming,
            u'评论时间': self.ping_lun_shi_jian,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论关键词': self.ping_lun_guan_jian_ci,
            u'评论类型': self.ping_lun_lei_xing,
            u'出游方式': self.chu_you_fang_shi,
            u'点赞数量': self.dian_zan_shu_liang,
            u'回复数量': self.hui_fu_shu_liang,
            u'成人票价格': self.cheng_ren_piao_jia_ge,
            u'老人票价格': self.lao_ren_piao_jia_ge,
            u'预定过程': self.yu_ding_guo_cheng,
            u'预订优惠': self.yu_ding_you_hui,
            u'取票便捷': self.qu_piao_bian_jie,
            u'景区': self.jing_qu,
            u'景区服务': self.jing_qu_fu_wu,
            u'行程': self.xing_cheng,
            u'导游': self.dao_you,
            u'交通': self.jiao_tong,
            u'住宿': self.zhu_su,
            u'返还': self.fan_huan,
            u'送积分': self.song_ji_fen
        }