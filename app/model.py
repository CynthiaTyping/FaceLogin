# coding: UTF-8
# @Time    : 2023/10/30
# @Author  : Qi Ming
# @WeChat  : 19310619597
# @FileName: modl.py
# @Software: Pycharm
from . import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    path = db.Column(db.String(64))
