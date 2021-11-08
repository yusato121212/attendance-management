from django import forms
from .models import Attendance

# 勤怠入力フォーム(未使用)
class AttendanceForm(forms.ModelForm):
    class Meta:
            model = Attendance
            fields = ('in_work','out_work','note',)