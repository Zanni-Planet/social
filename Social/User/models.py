from django.db import models

# Create your models here.
class User(models.Model):
    # 基本信息
    phonenum = models.CharField(max_length=32) # ⼿机号
    nickname = models.CharField(max_length=32) # 昵称
    gender = models.BooleanField() # 性别
    birthday = models.DateTimeField() # 出⽣⽇
    avatar = models.ImageField() # 个⼈形象
    location = models.CharField(max_length=64) # 常居地
    # 更多信息
    dating_gender = models.BooleanField() # 匹配的性别
    dating_location = models.CharField(max_length=128)  # ⽬标城市
    max_distance = models.FloatField() # 最⼤查找范围
    min_distance = models.FloatField()  # 最⼩查找范围
    max_dating_age = models.IntegerField() # 最⼤交友年龄
    min_dating_age = models.IntegerField() # 最⼩交友年龄
    vibration = models.BooleanField() # 开启震动
    only_matched = models.BooleanField() # 不让为匹配的⼈看我的相册
    auto_play = models.BooleanField() # ⾃动播放视频

    class Meta:
        db_table = 'user'
