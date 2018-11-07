# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/18 14:45
@Author  : Young
@QQ      : 403353323 
@File    : login.py
@Software: PyCharm
"""
from flask_restful import Resource, reqparse
from app.util.util import Code, Util
from flask import session
from app.models import User


#  登陆视图类
class Login(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('user_name', type=str, location='json', required=True)
        self.post_parser.add_argument('password', type=str, location='json', required=True)
        self.post_args = self.post_parser.parse_args()

    def post(self):
        user = User.query.filter_by(user_name=self.post_args.get('user_name')).first()
        print(user)
        if not user:
            return Util.make_result(Code.NOT_FOUND, msg="user don't existed")
        if not user.verify_password(self.post_args.get('password')):
            return Util.make_result(Code.ERROR, msg='密码错误')
        session['user'] = user.user_json()
        return Util.make_result(data=user.user_json())
