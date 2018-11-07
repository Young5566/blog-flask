# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/18 16:26
@Author  : Young
@QQ      : 403353323 
@File    : auth_decorator.py
@Software: PyCharm
"""
import functools
from app.util.util import Util, Code
from app.models import User
from flask import g


def auth_decorator(request):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not request.headers.get('Token'):
                return Util.make_result(code=Code.TOKEN_ERROR, msg='请添加token')
            user = User.confirm(request.headers.get('Token'))
            print(user)
            if not user:
                return Util.make_result(code=Code.TOKEN_ERROR, msg=Code.msg[Code.TOKEN_ERROR])
            g.user = user
            return func(*args, **kwargs)
        return wrapper
    return decorator