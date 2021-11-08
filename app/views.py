from datetime import datetime
from django.core.checks import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Attendance
from django.utils import timezone
from django.utils.timezone import localtime
from . import month

# 勤怠一覧
@login_required
def attendance_list(request):
    attendance_create(request,month.month_list())                                                             # 1ヶ月分のタイムカード作成
    attendances = Attendance.objects.filter(user=request.user).order_by('date')                               # filter:ログインユーザー,order_by:日付順
    today = month.today()                                                                                     # 今日の日付
    st_dt,ed_dt = month.monthly()                                                                             # タイムカードの月度
    return render(request,'app/attendance_list.html',{'attendances':attendances,'today':today,'st_dt':st_dt}) # 勤怠一覧を表示

# 出社時刻
def add_in_work(request,pk):
    obj = get_object_or_404(Attendance,pk=pk)   # 指定したpkのレコード取得
    obj.in_work = localtime(timezone.now())     # 出社時刻を格納 (localtimeで日本時刻に変換)
    obj.save()                                  # レコード保存
    return redirect('attendance_list')          # 勤怠一覧に戻る

# 退社時刻
def add_out_work(request,pk):
    obj = get_object_or_404(Attendance,pk=pk)   # 指定したpkのレコード取得
    obj.out_work = localtime(timezone.now())    # 退社時刻を格納 (localtimeで日本時刻に変換)
    obj.save()                                  # レコード保存
    return redirect('attendance_list')          # 勤怠一覧に戻る

# 1ヶ月分のタイムカードを作成
def attendance_create(request,dt_list):
    for dt in dt_list:
        Attendance.objects.get_or_create(user=request.user,date=dt)
