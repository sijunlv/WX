# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldGenerator.FieldBase import FieldBase

class huo_che_piao_shu_ju(FieldBase):
    def __init__(self, datasource, version=1, *args, **kwargs):
        FieldBase.__init__(self, datasource, version)
        self.chu_fa_di = None
        self.mu_di_di = None
        self.chu_fa_ri_qi = None
        self.che_ci = None
        self.chu_fa_zhan = None
        self.dao_da_zhan = None
        self.chu_fa_shi_jian = None
        self.dao_da_shi_jian = None
        self.li_shi = None
        self.shang_wu_zuo = None
        self.te_deng_zuo = None
        self.yi_deng_zuo = None
        self.er_deng_zuo = None
        self.gao_ji_ruan_wo = None
        self.ruan_wo = None
        self.ying_wo = None
        self.ruan_zuo = None
        self.ying_zuo = None
        self.wu_zuo = None
        self.qi_ta = None
        self.yong_hu_ming = None
        self.lu_xian = None
        self.gou_mai_shu_liang = None
        self.gou_mai_shi_jian = None

    def makemap(self):
        return {
            u'出发地': self.chu_fa_di,
            u'目的地': self.mu_di_di,
            u'出发日期': self.chu_fa_ri_qi,
            u'车次': self.che_ci,
            u'出发站': self.chu_fa_zhan,
            u'到达站': self.dao_da_zhan,
            u'出发时间': self.chu_fa_shi_jian,
            u'到达时间': self.dao_da_shi_jian,
            u'历史': self.li_shi,
            u'商务座': self.shang_wu_zuo,
            u'特等座': self.te_deng_zuo,
            u'一等座': self.yi_deng_zuo,
            u'二等座': self.er_deng_zuo,
            u'高级软卧': self.gao_ji_ruan_wo,
            u'软卧': self.ruan_wo,
            u'硬卧': self.ying_wo,
            u'软座': self.ruan_zuo,
            u'硬座': self.ying_zuo,
            u'无座': self.wu_zuo,
            u'其他': self.qi_ta,
            u'用户名': self.yong_hu_ming,
            u'路线': self.lu_xian,
            u'购买数量': self.gou_mai_shu_liang,
            u'购买时间': self.gou_mai_shi_jian
        }