from django.db import models

# Create your models here.


class User(models.Model):
    # 基本信息
    GENDERS = (
        ('male','小哥哥'),
        ('female', '小姐姐')
    )
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ("武汉", "武汉"),
        ("沈阳", "沈阳")
    )
    phonenum = models.CharField(max_length=32,unique=True)  # ⼿机号
    nickname = models.CharField(max_length=32,db_index=True)  # 昵称
    gender = models.CharField(max_length=10,choices=GENDERS,default='female')  # 性别
    birthday = models.DateField(default='1990-01-01')  # 出⽣⽇
    avatar = models.CharField(max_length=256,default='xxx')  # 个⼈形象
    location = models.CharField(max_length=64, choices=LOCATIONS,default='北京')  # 常居地

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.gender,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }

    class Meta:
        db_table = 'user'


class More(models.Model):
    # 更多信息
    uid = models.IntegerField() # 对应的用户ID
    dating_gender = models.BooleanField(default=0)  # 匹配的性别
    dating_location = models.CharField(max_length=128,default='北京')  # ⽬标城市
    max_distance = models.FloatField(default=10)  # 最⼤查找范围
    min_distance = models.FloatField(default=1)  # 最⼩查找范围
    max_dating_age = models.IntegerField(default=50)  # 最⼤交友年龄
    min_dating_age = models.IntegerField(default=18)  # 最⼩交友年龄
    vibration = models.BooleanField(default=True)  # 开启震动
    only_matched = models.BooleanField(default=True)  # 不让为匹配的⼈看我的相册
    auto_play = models.BooleanField(default=False)  # ⾃动播放视频

    def to_dict(self):
        return {
            'dating_gender':self.dating_gender,
            'dating_location':self.dating_location,
            'max_distance':self.max_distance,
            'min_distance':self.min_distance,
            'max_dating_age':self.max_dating_age,
            'min_dating_age':self.min_dating_age,
            'vibration':self.vibration,
            'only_matched':self.only_matched,
            'auto_play':self.auto_play
        }

    class Meta:
        db_table = 'more'
