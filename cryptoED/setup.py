#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : garlic
# @Time   : 2020/2/3 下午7:09

from setuptools import setup
setup(
    name='cryptoED',
    version='1.3',
    description='这是一个密码命令行工具',
    author='garlic',
    author_email='15027294155@163.com',
    py_modules=['cryptoED'],
    install_requires=[
        'click',
        'chardet',
        'numpy',
    ],
    entry_points='''
        [console_scripts]
        cryptoED=cryptoED:crypto
    ''',
)

