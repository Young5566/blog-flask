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
from app.api_1_0.article.post_article import PostArticle
from app.api_1_0.article.delete_article import DeleteArticle
from app.api_1_0.article.get_article import GetOneArticle, GetAllArticle, GetArticleByTag, GetAllTag

article = Blueprint('article', __name__)
source = Api(article)

source.add_resource(PostArticle, '/postArticle', endpoint='post_article')
source.add_resource(DeleteArticle, '/deleteArticle/<string:article_uuid>', endpoint='delete_article')
source.add_resource(GetOneArticle, '/getOneArticle/<string:article_uuid>', endpoint='get_one_article')
source.add_resource(GetAllArticle, '/getAllArticle', endpoint='get_all_article')
source.add_resource(GetArticleByTag, '/getArticleByTag', endpoint='get_article_by_tag')
source.add_resource(GetAllTag, '/getAllTag', endpoint='get_all_tag')