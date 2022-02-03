need_minutes = int(input())
h = int(input())
m = int(input())
need_minutes_ = need_minutes + h * 60 + m
hours = need_minutes_//60
minutes = need_minutes_%60
print(hours)
print(minutes)