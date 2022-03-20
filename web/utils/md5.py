# -*- encoding: utf-8 -*-
"""
@File    : md5.py
@Time    : 2022/2/27 21:45
@Author  : simon
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import hashlib


def gen_md5(origin):
    """
    md5加密
    :param origin:
    :return:
    """
    ha = hashlib.md5(b'jk3usodfjwkrsdf')
    ha.update(origin.encode('utf-8'))
    return ha.hexdigest()
