﻿注意事项

1.初始化的时候，必须传入数据源；
2.必须对id属性进行赋值；
3.在插入数据库之前必须要调用make()方法；
4.评论数据与基本数据分表存储的时候，可以通过调用make()方法后，获得uuid属性的值，作为关联字段
5.必须要判断 make() 的返回值，如果为空，那么获取数据就失败了；
6.FieldBase基类里面默认有一些字段，如原始数据：self.rawdata，可以对它进行赋值，保存一些原文信息；
7.FieldBase会自动生成uptime和do_time的值，无需自行赋值；
8.不推荐工厂类初始化后直接create()字段对象，建议在每次对字段属性赋值前才进行create()字段对象，也就是保证字段对象为局部变量，不建议其作为全局变量。