from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from mongoengine import connect, Document, EmbeddedDocument, \
    StringField, IntField, FloatField, DateTimeField, ListField, \
    EmbeddedDocumentField


# connect('students')
# connect('students', host='192.168.1.35', port=27017)
connect('students', host='mongodb://localhost/students')

class Grade(EmbeddedDocument):
    ''' 学生的成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOICES = (
        ('female', '女'),
        ('male', '男')
    )

class Student(Document):
    ''' 学生模型 '''
    name = StringField(required=True, max_lenght=32)
    age = IntField(required=True)
    sex = StringField(required=True, choices=SEX_CHOICES)
    grade = FloatField()
    created_at = DateTimeField(default=datetime.now())
    grades = ListField(EmbeddedDocumentField(Grade))
    address = StringField()
    school = StringField()

    meta = {
        'collection': 'students'
    }


class TestMongoEngine(object):

    def add_one(self):
        ''' 新增数据 '''
        yuwen = Grade(
            name='语文',
            score=95
            )
        english = Grade(
            name='英语',
            score=89)
        stu_obj = Student(
            name='张三',
            age=21,
            sex='male',
            grades=[yuwen, english]
        )
        # stu_obj.test = 'OK'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        ''' 查询一条数据 '''
        return Student.objects.first()

    def get_more(self):
        ''' 查询多条数据 '''
        # return Student.objects
        return Student.objects.all()

    def get_one_from_oid(self, oid):
        ''' 查询指定ID的数据 '''
        return Student.objects.filter(id=oid).first()

    def update(self):
        ''' 修改数据 '''
        # 修改一条数据
        # rest = Student.objects.filter(sex='male').update_one(inc__age=1)
        # return rest
        # 修改多条数据
        rest = Student.objects.filter(sex='male').update(inc__age=1)
        return rest

    def delete(self):
        ''' 删除数据 '''
        # 删除一条数据
        rest = Student.objects.filter(sex='male').first().delete()
        # 删除多条数据
        rest = Student.objects.filter(sex='male').delete()
        return rest

def main():
    obj = TestMongoEngine()
    # rest = obj.add_one()
    # print(rest.id)

    # rest = obj.get_one()
    # print(rest.id)

    rest = obj.get_more()
    print(type(rest))
    for item in rest:
        print(item.id)

    # rest = obj.get_one_from_oid('593bb8e7fa3ebd091078d40e')
    # print(rest.name)

    # rest = obj.update()
    # print(rest)

    # rest = obj.delete()
    # print(rest)

if __name__ == '__main__':
    main()