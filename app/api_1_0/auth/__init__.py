# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/18 14:36
@Author  : Young
@QQ      : 403353323 
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Blueprint
from flask_restful import Api
from app.api_1_0.auth.login import Login

auth = Blueprint('auth', __name__)
source = Api(auth)

source.add_resource(Login, '/login', endpoint='login')