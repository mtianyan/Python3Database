#!/usr/bin/python
#coding=utf-8

"""
https://pypi.python.org/pypi/Flask-SQLAlchemy
http://flask-sqlalchemy.pocoo.org/2.1/
http://www.pythondoc.com/flask-sqlalchemy/config.html
http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types
"""
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy

from forms import NewsForm


app = Flask(__name__)
db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    is_valid = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    news_type = db.Column(db.Enum('推荐', '百家', '本地', '图片'))

    comments = db.relationship('Comments', backref='news',
                                lazy='dynamic')

    def __repr__(self):
        return '<News %r>' % self.title


class Comments(db.Model):
    """ 新闻评论 """

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000), nullable=False)
    is_valid = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    new_id = db.Column(db.Integer, db.ForeignKey('news.id'))

    def __repr__(self):
        return '<News %r>' % self.content


@app.route('/')
def index():
    """ 新闻首页 """
    news_list = News.query.filter_by(is_valid=1)
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    news_list = News.query.filter_by(is_valid=1, news_type=name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情页 """
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    if page is None:
        page = 1
    page_data = News.query.filter_by(is_valid=1).paginate(page=page, per_page=4)
    return render_template("admin/index.html", page_data=page_data)


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """
    form = NewsForm()
    if form.validate_on_submit():
        n1 = News(
            title=form.title.data,
            content=form.content.data,
            img_url=form.img_url.data,
            news_type=form.news_type.data,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            )
        db.session.add(n1)
        db.session.commit()
        flash("新增成功")
        return redirect(url_for('admin'))
    return render_template("admin/add.html", form=form)


@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 新增新闻 """
    obj = News.query.get(pk)
    if obj is None:
        abort(404)
    form = NewsForm(obj=obj)
    if form.validate_on_submit():
        obj.title = form.title.data
        obj.content = form.content.data
        obj.news_type = form.news_type.data

        db.session.add(obj)
        db.session.commit()
        flash("修改成功")
        return redirect(url_for('admin'))
    return render_template("admin/update.html", form=form)


@app.route('/admin/delete/<int:pk>/', methods=['POST'])
def delete(pk):
    """ 新增新闻 """
    if request.method == 'POST':
        obj = News.query.get(pk)
        if obj is None:
            return 'no'
        obj.is_valid = False
        db.session.add(obj)
        db.session.commit()
        return 'yes'
    return 'no'


app.config['SQLALCHEMY_DATABASE_URI']  = 'mysql://root:123456@127.0.0.1/flask_news'
app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)