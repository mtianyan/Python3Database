#!/usr/bin/python
#coding=utf-8

"""
框架已经搭建好，大家自己实现
"""
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_mongoengine import MongoEngine

from forms import NewsForm


app = Flask(__name__)
# mongodb 数据库配置


NEWS_TYPES = (
    ('推荐', '推荐'),
    ('百家', '百家'),
    ('本地', '本地'),
    ('图片', '图片')
)

class News(db.Document):
    """ 新闻模型 """

   
    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """ 新闻首页 """
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<pk>/')
def detail(pk):
    """ 新闻详情页 """
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    return render_template("admin/index.html", page_data=page_data)


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """
    return render_template("admin/add.html", form=form)


@app.route('/admin/update/<pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 新增新闻 """
    return render_template("admin/update.html", form=form)


@app.route('/admin/delete/<pk>/', methods=['POST'])
def delete(pk):

    return 'no'


app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)