# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class da_qi_api_yun_ying_shang_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.shu_ju_lei_xing = None
        self.shu_ju_lai_yuan = None
        self.tui_song_shi_jian = None
        self.you_ke_zong_shu = None
        self.ming_cheng = None
        self.xing_zheng_dai_ma = None
        self.you_ke_lai_yuan_di = None
        self.tian_bao_lei_xing = None
        self.mu_di_di_xing_zheng_dai_ma = None
        self.tui_ru_shi_jian = None

    def makemap(self):
        return {
            u'数据类型': self.shu_ju_lei_xing,
            u'数据来源': self.shu_ju_lai_yuan,
            u'推送时间': self.tui_song_shi_jian,
            u'游客总数': self.you_ke_zong_shu,
            u'名称': self.ming_cheng,
            u'行政代码': self.xing_zheng_dai_ma,
            u'游客来源地': self.you_ke_lai_yuan_di,
            u'填报类型': self.tian_bao_lei_xing,
            u'目的地行政代码': self.mu_di_di_xing_zheng_dai_ma,
            u'推入时间': self.tui_ru_shi_jian
        }