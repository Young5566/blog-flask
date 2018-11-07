# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/16 8:30
@Author  : Young
@QQ      : 403353323 
@File    : config.py
@Software: PyCharm
"""
import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # 每次请求完自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ARTICLE_PER_PAGE = 10,

    # 配置类可以定义init_app()类方法。在这个方法中，可以执行对当前环境的配置初始化。
    # 现在基类Config中的init_app()方法为空
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/blog'


config = {
    'default': DevelopmentConfig
}