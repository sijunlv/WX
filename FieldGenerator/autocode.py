# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import getopt
import pypinyin

# Global config dict
CONFIG = {}

# 分割符
SEP = '_'

nummap = {
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu'
}

def show_help():
    print """\
Syntax: python %s <options>
 -c <className>    the class name
 -h                show this help screen
 -f <filePath>     the fieldname file
""" % sys.argv[0]


def parse_options(opts):
    global CONFIG
    opts = dict([(k.lstrip('-'), v) for (k, v) in opts])
    if 'h' in opts:
        show_help()
        exit(0)
    if 'c' in opts:
        CONFIG['classname'] = opts['c']
    if 'f' in opts:
        CONFIG['filename'] = opts['f']


# 从文件读取字段名列表
def get_field_list():
    global CONFIG
    f = open(CONFIG['filename'])
    return map(lambda x: x.replace('\xef\xbb\xbf', '').strip(), filter(lambda x: x.strip(), f))


def process():
    global nummap
    global SEP
    fields = get_field_list()
    pinyins = map(lambda x: x.replace('__', '_'), map(lambda x: filter(lambda x: x if x.isalnum() or x == SEP else '', x), map(lambda x: nummap[x[0]] + SEP + x[1:] if x[0].isdigit() else x, map(lambda x: pypinyin.slug(x.decode('utf-8'), separator=SEP), fields))))
    set_ = set(pinyins)
    if len(pinyins) != len(set_):
        dict_ = dict(zip(list(set_), [0] * len(set_)))
        for pinyin in pinyins:
            dict_[pinyin] += 1
        for key in dict_.keys():
            if dict_[key] > 1:
                print 'the same name: %s' % key
        raise Exception('variables having the same name')
    make(fields, pinyins)


# 生成代码文件
def make(fields, pinyins):
    global CONFIG
    f = open('%s.py' % CONFIG['classname'], 'w')
    txt = ''
    txt += '# -*- coding: utf-8 -*-' + '\n'
    txt += '__author__ = \'Lvv\'' + '\n'
    txt += '\n'
    txt += 'import sys' + '\n'
    txt += 'reload(sys)' + '\n'
    txt += 'sys.setdefaultencoding(\'utf-8\')' + '\n'
    txt += '\n'
    txt += 'from FieldGenerator.FieldBase import FieldBase' + '\n'
    txt += '\n'
    txt += 'class %s(FieldBase):' % CONFIG['classname'] + '\n'
    txt += '    def __init__(self, datasource, version=1, *args, **kwargs):' + '\n'
    txt += '        FieldBase.__init__(self, datasource, version)' + '\n'
    txt += '        ' + '\n        '.join(map(lambda x: 'self.%s = None' % x, pinyins))
    txt += '\n'
    txt += '\n'
    txt += '    def makemap(self):' + '\n'
    txt += '        return {' + '\n'
    txt += '            ' + '\n            '.join(map(lambda x: 'u\'%s\': self.%s,' % (x[0], x[1]), zip(fields[:-1], pinyins[:-1])))
    txt += '\n            ' + 'u\'%s\': self.%s' % (fields[-1], pinyins[-1]) + '\n'
    txt += '        }'
    txt = txt.replace('_shuai', '_lv')
    f.write(txt)
    f.close()

if '__main__' == __name__:
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'c:hf:')
    except getopt.GetoptError, e:
        print str(e)
        show_help()
        sys.exit(1)
    parse_options(opts)
    process()
