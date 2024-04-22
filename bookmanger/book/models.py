from django.db import models

# Create your models here.
"""
1.我们的模型类需要继承 models.Model
2.系统会为我们自动添加一个主键id
3.字段
    字段名=model.类型(选项
    这里的字段名就是数据表的字段
    不要去使用mysql、python关键字
    
    char(M)
    char(M)
    M 就是选项
"""


class BookInfo(models.Model):
    # id不用写
    name = models.CharField(max_length=10)


# 人物表先复制过来
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

