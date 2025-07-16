import math
import random
import os
import datetime

#* math
print(math.log10(100))
# 2.0
print(math.cos(0))
# 1.0
print(math.pi)
# 3.141592653589793

print("------------")

#* random
#? random.random(): 0.0 ~ 1.0 사이의 수를 랜덤으로 반환
print(random.random())
# 0.7890026947212738

#? random.randint(): 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수
print(random.randint(1, 20))
# 9

#? random.uniform(): 두 수 사이의 랜덤한 소수를 리턴하는 함수
print(random.uniform(0, 1))
# 0.804238787132

print("------------")

#* os
print(os.getlogin())
# chose
print(os.getcwd())
# C:\Users\chose\Desktop\공부\Python_applications\02

print("------------")

#* datetime
#? 2020년 3월 14일을 파이썬으로 표현
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
# 2020-03-14 00:00:00
print(type(pi_day))
# <class 'datetime.datetime'>

#? 시간 직접 설정
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
# 2020-03-14 13:06:15
print(type(pi_day))
# <class 'datetime.datetime'>

#? 오늘 날짜
pi_day = datetime.datetime.now()
print(pi_day)
# 2025-07-16 22:54:11.418816
print(type(pi_day))
# <class 'datetime.datetime'>

#? 두 datetime 값 사이의 기간
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
# 1950 days, 9:49:46.572005
print(type(today - pi_day))
# <class 'datetime.timedelta'>

#? timedelta(): timedelta를 생성해서 datetime 값에 더할 수도 있음
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)
# 2025-07-17 00:05:19.357393
print(today + my_timedelta)
# 2025-07-22 03:16:09.357393

#? datetime 해부하기
today = datetime.datetime.now()

print(today)
# 2025-07-17 00:07:12.293553
print(today.year)
# 2025
print(today.month)
# 7
print(today.day)
# 17
print(today.hour)
# 0
print(today.minute)
# 7
print(today.second)
# 12
print(today.microsecond)
# 293553

#? datetime 포매팅(strftime())
today = datetime.datetime.now()

print(today)
# 2025-07-17 00:10:47.095915
print(today.strftime("%A, %B %dth %Y"))
# Thursday, July 17th 2025

# %a	요일 (짧은 버전)	               Mon
# %A	요일 (풀 버전)	                   Monday
# %w	요일 (숫자 버전, 0~6, 0이 일요일)   5
# %d	일 (01~31)	                      23
# %b	월 (짧은 버전)	                   Nov
# %B	월 (풀 버전)	                   November
# %m	월 (숫자 버전, 01~12)	           10
# %y	연도 (짧은 버전)	               16
# %Y	연도 (풀 버전)	                   2016
# %H	시간 (00~23)	                  14
# %I	시간 (00~12)	                  10
# %p	AM/PM	                          AM
# %M	분 (00~59)	                      34
# %S	초 (00~59)	                      12
# %f	마이크로초 (000000~999999)	       413215
# %Z	표준시간대	                       PST
# %j	1년 중 며칠째인지 (001~366)	       162
# %U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35