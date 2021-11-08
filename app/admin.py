from django.contrib import admin
from .models import Attendance

# 管理画面から見られるようにする
admin.site.register(Attendance)

