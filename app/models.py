# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/16 8:34
@Author  : Young
@QQ      : 403353323 
@File    : models.py
@Software: PyCharm
"""
from app import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import *
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from uuid import uuid4
import time


class User(db.Model):
    __tablename__ = 'user'

    user_uuid = db.Column(db.String(64), primary_key=True, nullable=False)
    user_name = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64))
    head_img = db.Column(db.String(256))
    article = db.relationship('Article', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.user_name

    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，
    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
    # 于是，我们就拥有一个可控的属性操作
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'user_uuid': self.user_uuid})

    @staticmethod
    def confirm(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            token_data = s.loads(token)
        except:
            print('token 过期')
            return None
        user = User.query.get(token_data.get('user_uuid'))
        return user

    def user_json(self):
        user_info = {
            "user_uuid": self.user_uuid,
            "user_name": self.user_name,
            "email": self.email,
            "head_img": self.head_img,
            "token": self.generate_confirmation_token()
        }

        return user_info


class Article(db.Model):
    __tablename__ = 'article'

    article_uuid = db.Column(db.String(64), primary_key=True, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(64), nullable=False)
    second_tags = db.Column(db.String(64), nullable=False)
    author_uuid = db.Column(db.String(64), db.ForeignKey('user.user_uuid'))
    article_img = db.Column(db.String(128), nullable=False, default="http://pic1.win4000.com/wallpaper/2017-10-11/59ddb17491bcf.jpg")
    pub_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.title

    @staticmethod
    def generate_fake(count=100):
        import forgery_py
        for i in range(count):
            article_uuid = str(uuid4())
            title = '测试标题'
            abstract = '摘要英文摘要 编辑 这里要讨论的主要是中文科技论文所附的英文摘要,其内容包含题名、' \
                       '摘要及关键词。GB 7713—87规定,为了国际交流,科学技术报告、学位论文和学术'
            content = """<h2><a id="_0"></a>这里是标题测试</h2><table><thead><tr><th>column1</th><th>column2</th><th>column3</th></tr></thead><tbody><tr><td>content1</td><td>content2</td><td>content3</td></tr></tbody></table><p>这里是内容</p><pre><div class="hljs"><code class="lang-javaScript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这里是代码测试'</span>);</code></div></pre><h2><a id="_0"></a>这里是标题测试</h2><table><thead><tr><th>column1</th><th>column2</th><th>column3</th></tr></thead><tbody><tr><td>content1</td><td>content2</td><td>content3</td></tr></tbody></table><p>这里是内容</p><pre><div class="hljs"><code class="lang-javaScript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这里是代码测试'</span>);</code></div></pre>"""
            tags = 'Python'
            second_tags = 'flask'
            author_uuid = '8836ef61-162f-4bf5-a372-74eb3efdb182'
            pub_time = forgery_py.date.date(True)
            article = Article(
                article_uuid=article_uuid,
                title=title,
                abstract=abstract,
                content=content,
                tags=tags,
                second_tags=second_tags,
                author_uuid=author_uuid,
                article_img="http://pic1.win4000.com/wallpaper/2017-10-11/59ddb17491bcf.jpg",
                pub_time=pub_time
            )
            db.session.add(article)
            db.session.commit()

    def utc2local(self, utc_st):
        now_stamp = time.time()
        local_time = datetime.fromtimestamp(now_stamp)
        utc_time = datetime.utcfromtimestamp(now_stamp)
        offset = local_time - utc_time
        local_st = utc_st + offset
        return local_st

    def article_json(self):
        article_json = {
            "article_uuid": self.article_uuid,
            "title": self.title,
            "abstract": self.abstract,
            "content": self.content,
            "tags": self.tags,
            "second_tags": self.second_tags,
            "author": self.author.user_name,
            "article_img": self.article_img,
            # "pub_time": self.utc2local(self.pub_time).strftime("%Y-%m-%d %H:%M:%S")
            "pub_time": self.utc2local(self.pub_time).strftime("%Y-%m-%d")
        }
        return article_json
