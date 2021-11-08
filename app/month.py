from datetime import datetime,timedelta

# 日付一覧
def month_list():

    dt_list = []
    st_dt,ed_dt = monthly()

    # 日付格納
    cnt = 0
    while(True):
        dt = st_dt + timedelta(days=cnt)
        if dt <= ed_dt:
            dt_list.append(dt)
        else:
            break
        cnt = cnt+1
    return dt_list

# 前月(今月)の21日～今月(来月)20日を算出
def calc_day(dt_now,ofs_st,ofs_ed):
    st_str = '{0}/{1}/{2}'.format(dt_now.year,dt_now.month + ofs_st,21)
    st_dt = datetime.strptime(st_str,'%Y/%m/%d')
    ed_str = '{0}/{1}/{2}'.format(dt_now.year,dt_now.month + ofs_ed,20)
    ed_dt = datetime.strptime(ed_str,'%Y/%m/%d')
    return st_dt,ed_dt

# タイムカードが何月度か算出
def monthly():
    dt_now = today()

    # 日付算出
    if dt_now.day <= 20:
        st_dt,ed_dt = calc_day(dt_now,-1,0)   # 前月の21日～今月の20日
    else:
        st_dt,ed_dt = calc_day(dt_now,0,1)    # 今月の21日～来月の20日
    return st_dt,ed_dt

# 今日の日付
def today():
    return datetime.now()
