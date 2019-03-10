# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/18 15:54
@Author  : Young
@QQ      : 403353323 
@File    : post_article.py
@Software: PyCharm
"""

from flask_restful import reqparse, Resource
from app.models import Article
from app.util.util import Util, Code
from app import db
from app.api_1_0.decorators.auth_decorator import auth_decorator
from flask import request, g
from datetime import datetime


class PostArticle(Resource):
    method_decorators = [auth_decorator(request)]

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('title', type=str, location='json', required=True)
        self.post_parser.add_argument('content', type=str, location='json', required=True)
        self.post_parser.add_argument('tags', type=str, location='json', required=True)
        self.post_parser.add_argument('secondTags', type=str, location='json', required=True)
        self.post_parser.add_argument('image_uuid', type=str, location='json', required=True)
        self.post_parser.add_argument('abstract', type=str, location='json', required=True)
        self.post_args = self.post_parser.parse_args()

    def post(self):
        article = Article(
            article_uuid=Util.get_uuid(),
            title=self.post_args.get('title'),
            content=self.post_args.get('content'),
            tags=self.post_args.get('tags'),
            second_tags=self.post_args.get('secondTags'),
            article_img_uuid=self.post_args.get('image_uuid'),
            abstract=self.post_args.get('abstract'),
            author_uuid=g.get('user').user_uuid
        )
        db.session.add(article)
        try:
            db.session.commit()
        except:
            return Util.make_result(code=Code.SQL_ERROR, msg=Code.msg[Code.SQL_ERROR])
        return Util.make_result(msg='添加成功')