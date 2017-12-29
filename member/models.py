from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
    school_id = models.CharField(max_length=10, unique=True)  # 學號 | 教師證號
    school_voip = models.CharField(max_length=10, blank=True, null=True) # 校內分機
    name = models.CharField(max_length=30, blank=True, null=True) # 原始資料姓名
    remark = models.CharField(max_length=40, blank=True, null=True) # 標注
    email = models.EmailField(blank=True, null=True)
    fb = models.URLField(max_length=200, blank=True, null=True)      # Facebook 連結
    github = models.URLField(max_length=100, blank=True, null=True)  # GitHub 連結
    personal_web = models.URLField(max_length=200, blank=True, null=True)  # 個人網頁
    cellphone = models.CharField(max_length=10, blank=True, null=True)   # 手機
    counrty = models.CharField(max_length=10, blank=True, null=True)  #國家
    in_association = models.BooleanField(default=False) # 是否 為系學會成員
    is_buy_coat = models.BooleanField(default=False)    # 是否 買系外套
    is_buy_clothes = models.BooleanField(default=False) # 是否 買系衣服
    last_IP = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return self.school_id + ' ' + self.name


