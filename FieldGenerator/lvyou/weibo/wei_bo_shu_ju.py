# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class wei_bo_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.wei_bo_ming_cheng = None
        self.wei_bo_nei_rong = None
        self.wei_bo_shi_jian = None
        self.lai_zi = None
        self.shou_cang_shu = None
        self.zhuan_fa = None
        self.ping_lun = None
        self.dian_zan = None

    def makemap(self):
        return {
            u'微博名称': self.wei_bo_ming_cheng,
            u'微博内容': self.wei_bo_nei_rong,
            u'微博时间': self.wei_bo_shi_jian,
            u'来自': self.lai_zi,
            u'收藏数': self.shou_cang_shu,
            u'转发': self.zhuan_fa,
            u'评论': self.ping_lun,
            u'点赞': self.dian_zan
        }