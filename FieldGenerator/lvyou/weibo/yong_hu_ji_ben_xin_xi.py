# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class yong_hu_ji_ben_xin_xi(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.yong_hu_ming = None
        self.gong_zuo_jing_li = None
        self.xue_xi_jing_li = None
        self.suo_zai_di = None
        self.gan_qing_zhuang_tai = None
        self.lai_yuan_di = None
        self.chu_sheng_ri_qi = None
        self.hao_you_shu_liang = None
        self.guan_zhu_zhe_shu_liang = None

    def makemap(self):
        return {
            u'用户名': self.yong_hu_ming,
            u'工作经历': self.gong_zuo_jing_li,
            u'学习经历': self.xue_xi_jing_li,
            u'所在地': self.suo_zai_di,
            u'感情状态': self.gan_qing_zhuang_tai,
            u'来源地': self.lai_yuan_di,
            u'出生日期': self.chu_sheng_ri_qi,
            u'好友数量': self.hao_you_shu_liang,
            u'关注者数量': self.guan_zhu_zhe_shu_liang
        }