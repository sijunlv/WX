# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class guo_nei_mei_shi_ping_lun(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.cheng_shi = None
        self.dian_ming = None
        self.shang_hu_ping_fen = None
        self.ren_jun = None
        self.wu_xing_ping_fen_shu = None
        self.si_xing_ping_fen_shu = None
        self.san_xing_ping_fen_shu = None
        self.er_xing_ping_fen_shu = None
        self.yi_xing_ping_fen_shu = None
        self.kou_wei = None
        self.huan_jing = None
        self.fu_wu = None
        self.yong_hu_ming = None
        self.gong_xian_zhi = None
        self.ping_lun_nei_rong = None
        self.ting_che_xin_xi = None
        self.ping_lun_shi_jian = None

    def makemap(self):
        return {
            u'城市': self.cheng_shi,
            u'店名': self.dian_ming,
            u'商户评分': self.shang_hu_ping_fen,
            u'人均': self.ren_jun,
            u'五星评分数': self.wu_xing_ping_fen_shu,
            u'四星评分数': self.si_xing_ping_fen_shu,
            u'三星评分数': self.san_xing_ping_fen_shu,
            u'二星评分数': self.er_xing_ping_fen_shu,
            u'一星评分数': self.yi_xing_ping_fen_shu,
            u'口味': self.kou_wei,
            u'环境': self.huan_jing,
            u'服务': self.fu_wu,
            u'用户名': self.yong_hu_ming,
            u'贡献值': self.gong_xian_zhi,
            u'评论内容': self.ping_lun_nei_rong,
            u'停车信息': self.ting_che_xin_xi,
            u'评论时间': self.ping_lun_shi_jian
        }