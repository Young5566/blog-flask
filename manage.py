# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/16 8:29
@Author  : Young
@QQ      : 403353323 
@File    : manage.py.py
@Software: PyCharm
"""

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Shell
from app import create_app, db
from app.models import User, Article
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# make_context 这个参数的作用就是在启动的 shell 中添加默认的变量，例如上面添加了 db、User 这些，也就是说在你启动 shell
# 之后就可以直接像访问默认函数/变量一样直接什么都不用 import 就可以这样用：
def make_shell_context():
    return dict(app=app, User=User, Article=Article)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()