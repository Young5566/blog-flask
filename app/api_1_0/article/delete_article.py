# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/18 17:42
@Author  : Young
@QQ      : 403353323 
@File    : delete_article.py
@Software: PyCharm
"""
from app import db
from app.models import Article
from app.util.util import Code, Util
from flask_restful import Resource
from app.api_1_0.decorators.auth_decorator import auth_decorator
from flask import request


class DeleteArticle(Resource):
    method_decorators = [auth_decorator(request)]

    def delete(self, article_uuid):
        article = Article.query.filter_by(article_uuid=article_uuid).first()
        if not article:
            return Util.make_result(code=Code.NOT_FOUND, msg=Code.msg[Code.NOT_FOUND])
        db.session.delete(article)
        try:
            db.session.commit()
        except:
            return Util.make_result(code=Code.SQL_ERROR, msg=Code.msg[Code.SQL_ERROR])
        return Util.make_result()