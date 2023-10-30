# coding: UTF-8
# @Time    : 2023/10/30
# @Author  : Qi Ming
# @WeChat  : 19310619597
# @FileName: __init__.py
# @Software: Pycharm
from flask import Blueprint

web = Blueprint('web', __name__)
from . import view
