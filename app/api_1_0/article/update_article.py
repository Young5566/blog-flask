# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/16 20:37
@Author  : Young
@QQ      : 403353323 
@File    : update_article.py
@Software: PyCharm
"""

from flask_restful import Resource, reqparse
from app.util.util import Code, Util
from flask import request
from app.api_1_0.decorators.auth_decorator import auth_decorator
from app.models import Article
from app import db


class UpdateArticle(Resource):
    method_decorators = [auth_decorator(request)]

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('articleUuid', type=str, location='json', required=True)
        self.post_parser.add_argument('articleInfo', type=dict, location='json', required=True)
        self.post_args = self.post_parser.parse_args()

    def post(self):
        article = Article.query.filter_by(article_uuid=self.post_args.get('articleUuid')).first()
        if not article:
            return Util.make_result(code=Code.NOT_FOUND, msg='该文章不存在!')
        try:
            for key, value in self.post_args.get('articleInfo').items():
                article.__setattr__(key, value)
            # db.session.add(article)
            # db.session.commit()
        except:
            return Util.make_result(Code.SQL_ERROR, msg='修改失败')
        return Util.make_result()