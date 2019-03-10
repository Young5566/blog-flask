# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 17:02
@Author  : Young
@QQ      : 403353323 
@File    : add_image.py
@Software: PyCharm
"""

from flask_restful import reqparse, Resource
from app.models import Image
from app.util.util import Code, Util
from app.api_1_0.decorators.auth_decorator import auth_decorator
from flask import request
from app import db


class AddPicture(Resource):
    method_decorators = [auth_decorator(request)]

    def __init__(self):
        self.add_parser = reqparse.RequestParser()
        self.add_parser.add_argument('fileUuid', type=str, location='json', required=True)
        self.add_parser.add_argument('name', type=str, location='json', required=True)
        self.add_parser.add_argument('groupName', type=str, location='json', required=True)
        self.add_parser.add_argument('remoteFileId', type=str, location='json', required=True)
        self.add_parser.add_argument('storageIp', type=str, location='json', required=True)
        self.add_parser.add_argument('size', type=int, location='json', required=True)
        self.add_parser.add_argument('imageUrl', type=str, location='json', required=True)
        self.add_args = self.add_parser.parse_args()

    def post(self):
        image = Image(
            file_uuid = self.add_args.get("fileUuid"),
            image_uuid=Util.get_uuid(),
            name=self.add_args.get('name'),
            group_name=self.add_args.get('groupName'),
            remote_file_id=self.add_args.get('remoteFileId'),
            storage_ip=self.add_args.get('storageIp'),
            size=self.add_args.get('size'),
            image_url=self.add_args.get('imageUrl')
        )
        db.session.add(image)
        try:
            db.session.commit()
        except:
            return Util.make_result(code=Code.SQL_ERROR, msg=Code.msg[Code.SQL_ERROR])
        return Util.make_result(data=image.image_uuid, msg='添加成功')