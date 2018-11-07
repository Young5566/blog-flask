# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/16 9:10
@Author  : Young
@QQ      : 403353323 
@File    : util.py
@Software: PyCharm
"""
from flask import jsonify
import uuid


class Code:
    SUCCESS = 200
    PARAM_ERROR = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    ERROR = 700
    SQL_ERROR = 701
    TOKEN_ERROR = 703

    msg = {
        SUCCESS: '操作成功',
        PARAM_ERROR: '请求参数错误',
        SQL_ERROR: '数据库操作失败',
        NOT_FOUND: '没有该目标',
        TOKEN_ERROR: 'token过期或错误',
        UNAUTHORIZED: '没有添加token'
    }


class Util(object):

    @staticmethod
    def make_result(code=Code.SUCCESS, msg=Code.msg[Code.SUCCESS], data=None):
        """
        用于统一返回结果
        :param code: 状态码(默认为成功)
        :param msg: 信息说明（默认成功）
        :param data: 返回数据参数（默认空）
        """

        return jsonify({
            'code': code,
            'msg':  msg,
            'data': data
        })

    @staticmethod
    def get_uuid():
        return str(uuid.uuid4())
