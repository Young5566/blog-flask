# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/19 10:09
@Author  : Young
@QQ      : 403353323 
@File    : get_article.py
@Software: PyCharm
"""
from flask_restful import reqparse, Resource
from app.models import Article
from app.util.util import Code, Util
from flask import current_app


# 根据文章id查文章内容
class GetOneArticle(Resource):
    def get(self, article_uuid):
        article = Article.query.filter_by(article_uuid=article_uuid).first()
        if not article:
            return Util.make_result(Code.NOT_FOUND, msg=Code.msg[Code.NOT_FOUND])
        return Util.make_result(data=article.article_json())


# 查询全部文章
class GetAllArticle(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('page', type=int, location='args', default=1)
        self.get_parser.add_argument('per_page', type=int, location='args')
        self.get_args = self.get_parser.parse_args()

    def get(self):
        per_page = self.get_args.get('per_page')
        if not per_page:
            per_page = current_app.config['ARTICLE_PER_PAGE'][0]
        pagination = Article.query.order_by(Article.pub_time.desc())\
            .paginate(page=self.get_args.get('page'), per_page=per_page,error_out=False)
        articles = pagination.items
        return Util.make_result(data={
            'articles': [article.article_json() for article in articles],
            'total': pagination.total
        })


# 根据标签查文章
class GetArticleByTag(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('tag', type=str, location='args', required=True)
        self.get_parser.add_argument('page', type=int, location='args', default=1)
        self.get_args = self.get_parser.parse_args()

    def get(self):
        articles = Article.query.filter(Article.tags == self.get_args.get('tag')).all()
        article_titles = {}
        for article in articles:
            if article.second_tags not in article_titles:
                article_titles[article.second_tags] = []
            article_titles[article.second_tags].append({
                'id': article.article_uuid,
                'title': article.title
            })

        return Util.make_result(data=article_titles)


# 查询所有标签
class GetAllTag(Resource):
    def get(self):
        result_tags = Article.query.with_entities(Article.tags).distinct().all()
        tags = [tag[0] for tag in result_tags]
        return Util.make_result(data={'tags': tags})