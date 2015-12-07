# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from FieldFactory import FieldFactory
from myssdb import myssdb

sys.path.append('./lvyou/jipiao')

if __name__ == '__main__':
    # 携程国内机票爬虫例子

    # 1 实例化工厂类以及ssdb对象
    fieldfactory = FieldFactory(datasource=u'携程', version=2)
    ssdb = myssdb(table='xiecheng_test', host='web12', port=54321)

    # 2 由类名创建字段对象
    field = fieldfactory.create('guo_nei_ji_piao')

    # 3 根据国内机票类对字段逐一进行赋值
    field.id = u'G52730'
    field.jia_ge = 888
    field.ban_qi = [1, 2, 5]
    # ......

    # 4 生成数据表
    data = field.make()

    # 调用make方法后，可以获取uuid
    # print 'uuid: %s' % field.uuid
    # print data

    # 5 插入ssdb
    if data:
        ssdb.put(data)
        print 'save success'
    else:
        print 'data is null'


