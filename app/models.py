from django.db import models
from django.conf import settings
from django.utils import timezone

# 出退勤
class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="ユーザー") # 管理者ユーザーとの紐付け
    date = models.DateField(verbose_name="日付")                                                        # 日付
    in_work = models.TimeField(blank=True,null=True,verbose_name="出社")                                # 出勤時刻(任意,null)
    out_work = models.TimeField(blank=True,null=True,verbose_name="退社")                               # 退勤時刻(任意,null)
    note = models.CharField(max_length=50,blank=True,default="",verbose_name="備考")                    # 備考(任意,空文字)

    # レコード名
    def __str__(self):
        return ("{0}-{1}".format(self.date,self.user))