from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
    school_id = models.CharField(max_length=10, unique=True)  # 學號 | 教師證號   
    name = models.CharField(max_length=30, blank=True, null=True) # 原始資料姓名
    remark = models.CharField(max_length=40, blank=True, null=True) # 標注
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return self.school_id + ' ' + self.name

class loginInfo(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        null=True
    )
    last_IP = models.GenericIPAddressField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

class contact(models.Model):
    data = models.CharField(max_length=100)      # Facebook, GitHub 連結, 手機
    category = models.IntegerField()          # 1 FB, 2 GitHub, 3 cellphone, 4 校內分機, 5 email
    member = models.ForeignKey('Member', on_delete=models.CASCADE)

class SAM(models.Model):
    is_buy_coat = models.BooleanField(default=False)    # 是否 買系外套
    is_buy_clothes = models.BooleanField(default=False) # 是否 買系衣服
    enroll_date = updated_at = models.DateTimeField(blank=True, null=True)
    leave_date = updated_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE, null=True)
