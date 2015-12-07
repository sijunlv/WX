# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_wai_gou_wu(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.fen_lei = None
        self.dian_ming = None
        self.shang_cheng_di_zhi = None
        self.ping_fen = None
        self.ping_lun_shu = None
        self.xiao_fei = None
        self.di_zhi = None
        self.te_se = None
        self.ying_ye_shi_jian = None
        self.ting_che_xin_xi = None
        self.chan_pin = None
        self.huan_jing = None
        self.fu_wu = None
        self.pai_ming = None
        self.shang_hu = None
        self.shang_qu = None
        self.ren_jun = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'分类': self.fen_lei,
            u'店名': self.dian_ming,
            u'商城地址': self.shang_cheng_di_zhi,
            u'评分': self.ping_fen,
            u'评论数': self.ping_lun_shu,
            u'消费': self.xiao_fei,
            u'地址': self.di_zhi,
            u'特色': self.te_se,
            u'营业时间': self.ying_ye_shi_jian,
            u'停车信息': self.ting_che_xin_xi,
            u'产品': self.chan_pin,
            u'环境': self.huan_jing,
            u'服务': self.fu_wu,
            u'排名': self.pai_ming,
            u'商户': self.shang_hu,
            u'商区': self.shang_qu,
            u'人均': self.ren_jun
        }