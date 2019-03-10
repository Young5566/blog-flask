# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 18:25
@Author  : Young
@QQ      : 403353323 
@File    : delete_image.py
@Software: PyCharm
"""

from flask_restful import Api, Resource
from flask import request
from app.util.util import Code, Util
from app.api_1_0.decorators.auth_decorator import auth_decorator
from app.models import Image
from app import db


class DeleteImage(Resource):
    method_decorators = [auth_decorator(request)]

    def delete(self, image_uuid):
        image = Image.query.filter_by(image_uuid=image_uuid).first()
        if not image:
            return Util.make_result(code=Code.NOT_FOUND, msg=Code.msg[Code.NOT_FOUND])
        db.session.delete(image)
        try:
            db.session.commit()
        except:
            return Util.make_result(code=Code.SQL_ERROR, msg='删除图片失败')

        return Util.make_result()