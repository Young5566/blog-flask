# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 17:02
@Author  : Young
@QQ      : 403353323 
@File    : get_image.py
@Software: PyCharm
"""

from flask_restful import Resource, reqparse
from app.util.util import Code, Util
from app.api_1_0.decorators.auth_decorator import auth_decorator
from flask import request, current_app
from app.models import Image


class GetAllImage(Resource):
    method_decorators = [auth_decorator(request)]

    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('page', type=int, location='args', default=1)
        self.get_parser.add_argument('per_page', type=int, location='args')
        self.get_args = self.get_parser.parse_args()

    def get(self):
        per_page = self.get_args.get('per_page')
        if not per_page:
            per_page = current_app.config['ARTICLE_PER_PAGE'][0]
        pagination = Image.query.order_by(Image.create_time.desc())\
            .paginate(page=self.get_args.get('page'), per_page=per_page, error_out=False)
        images = pagination.items
        return Util.make_result(data={
            'images': [image.image_json() for image in images],
            'total': pagination.total
        })


class GetOneImage(Resource):
    method_decorators = [auth_decorator(request)]

    def get(self, image_uuid):
        image = Image.query.filter_by(image_uuid=image_uuid).first()
        if not image:
            return Util.make_result(Code.NOT_FOUND, msg=Code.msg[Code.NOT_FOUND])
        return Util.make_result(data=image.image_detail_json())