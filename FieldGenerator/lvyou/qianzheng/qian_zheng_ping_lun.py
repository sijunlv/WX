# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class qian_zheng_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.chan_pin_ming_cheng = None
        self.qian_zheng_guo_jia = None
        self.hu_zhao_qian_fa_di_chang_zhu_di = None
        self.qian_zheng_tao_can = None
        self.zong_he_ping_fen = None
        self.xiao_shou_dian_pu = None
        self.ping_lun_nei_rong = None
        self.ping_lun_shi_jian = None
        self.yong_hu_ming = None
        self.xing_hao = None
        self.chan_pin_bian_hao = None
        self.chu_xing_fang_shi = None
        self.ban_li_liu_cheng = None
        self.fu_wu_tai_du = None
        self.xin_xi_fan_kui = None
        self.qi_ta = None
        self.deng_ji = None
        self.ping_lun_lai_yuan = None

    def makemap(self):
        return {
            u'产品名称': self.chan_pin_ming_cheng,
            u'签证国家': self.qian_zheng_guo_jia,
            u'护照签发地/常住地': self.hu_zhao_qian_fa_di_chang_zhu_di,
            u'签证套餐': self.qian_zheng_tao_can,
            u'综合评分': self.zong_he_ping_fen,
            u'销售店铺': self.xiao_shou_dian_pu,
            u'评论内容': self.ping_lun_nei_rong,
            u'评论时间': self.ping_lun_shi_jian,
            u'用户名': self.yong_hu_ming,
            u'型号': self.xing_hao,
            u'产品编号': self.chan_pin_bian_hao,
            u'出行方式': self.chu_xing_fang_shi,
            u'办理流程': self.ban_li_liu_cheng,
            u'服务态度': self.fu_wu_tai_du,
            u'信息反馈': self.xin_xi_fan_kui,
            u'其他': self.qi_ta,
            u'等级': self.deng_ji,
            u'评论来源': self.ping_lun_lai_yuan
        }