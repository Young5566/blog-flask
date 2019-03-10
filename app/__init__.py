# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/16 8:34
@Author  : Young
@QQ      : 403353323 
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Flask, abort
import flask_restful
import pymysql
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.util.util import Code, Util
from flask_cors import *

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def custom_abort(http_status_code, *args, **kwargs):
    if http_status_code == 400:
        abort(Util.make_result(code=Code.PARAM_ERROR, msg=Code.msg[Code.PARAM_ERROR]))

    return abort(http_status_code)


flask_restful.abort = custom_abort


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from app.api_1_0.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1.0/auth')

    from app.api_1_0.article import article as article_blueprint
    app.register_blueprint(article_blueprint, url_prefix='/api/v1.0/article')

    from app.api_1_0.image import image as image_blueprint
    app.register_blueprint(image_blueprint, url_prefix='/api/v1.0/image')

    return app




