#!/usr/bin/python
#coding=utf-8

"""
框架已搭建好，请大家自己实现
"""
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request


from forms import NewsForm


app = Flask(__name__)
db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """

    def __repr__(self):
        return '<News %r>' % self.title



@app.route('/')
def index():
    """ 新闻首页 """
    return render_template("index.html")


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    return render_template('cat.html')


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情页 """
    return render_template('detail.html')


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    return render_template("admin/index.html")


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """
    return render_template("admin/add.html")


@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 新增新闻 """
    return render_template("admin/update.html")


@app.route('/admin/delete/<int:pk>/', methods=['POST'])
def delete(pk):
    return 'no'


app.config['SQLALCHEMY_DATABASE_URI']  = ''
app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)