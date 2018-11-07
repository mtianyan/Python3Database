#!/usr/bin/python
#coding=utf-8

"""
http://flask-mongoengine.readthedocs.io/en/latest/
"""
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_mongoengine import MongoEngine

from forms import NewsForm


app = Flask(__name__)
# mongodb 数据库配置
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_news',
    'host': '127.0.0.1',
    # 'username':'webapp',
    # 'password':'pwd123'
    'port': 27017
}
db = MongoEngine(app)

NEWS_TYPES = (
    ('推荐', '推荐'),
    ('百家', '百家'),
    ('本地', '本地'),
    ('图片', '图片')
)

class News(db.Document):
    """ 新闻模型 """

    title = db.StringField(required=True, max_length=200)
    img_url = db.StringField()
    content = db.StringField()
    is_valid = db.BooleanField(default=True)
    created_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())
    news_type = db.StringField(required=True, choices=NEWS_TYPES)

    meta = {
        'collection': 'news'
    }

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """ 新闻首页 """
    news_list = News.objects.filter(is_valid=True)
    print(news_list.count)
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    news_list = News.objects.filter(is_valid=True, news_type=name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<pk>/')
def detail(pk):
    """ 新闻详情页 """
    new_obj = News.objects.filter(pk=pk).first()
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    if page is None:
        page = 1
    page_data = News.objects.filter(is_valid=True).paginate(page=page, per_page=4)
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
            news_type=form.news_type.data
            )
        n1.save()
        flash("新增成功")
        return redirect(url_for('admin'))
    return render_template("admin/add.html", form=form)


@app.route('/admin/update/<pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 新增新闻 """
    obj = News.objects.filter(pk=pk).first()
    if obj is None:
        abort(404)
    form = NewsForm(obj=obj)
    if form.validate_on_submit():
        obj.title = form.title.data
        obj.content = form.content.data
        obj.news_type = form.news_type.data

        obj.save()
        flash("修改成功")
        return redirect(url_for('admin'))
    return render_template("admin/update.html", form=form)


@app.route('/admin/delete/<pk>/', methods=['POST'])
def delete(pk):
    """ 新增新闻 """
    if request.method == 'POST':
        obj = News.objects.filter(pk=pk).first()
        if obj is None:
            return 'no'
        obj.is_valid = False
        obj.save()
        return 'yes'
    return 'no'


app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)