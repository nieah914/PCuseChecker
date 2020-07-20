#-*- coding: utf-8 -*-
import datetime
from datetime import timedelta
import Evtx.Evtx as evtx
from bs4 import BeautifulSoup
import pytz
import time

f = open('이벤트.txt','r', encoding= "utf-8" )

# print(type(Thistime)) # [class 'datetime.datetime']
# print(myDatetime)       # 2018-07-28 12:11:32
total_time = []
isInitial = True
timezone = pytz.timezone('Asia/Seoul')
path = "C:\Windows\System32\winevt\Logs\Application.evtx"
# level 2 : 오류
# level 3 : 경고
# level 4 : 정보
with evtx.Evtx(path) as log:
    for x in range(1000,3000):
        RecordOBJ = log.get_record(x)
        soup = BeautifulSoup(RecordOBJ.xml(),"lxml")
        # print(soup)
        ext_time = soup.find('timecreated')['systemtime'][:-7]
        Thistime = datetime.datetime.strptime(ext_time,'%Y-%m-%d %H:%M:%S') + timedelta(hours=9)
        # print(ko_time)
        # print("=========================================")
        # timezone.localize(datetime.datetime(soup.find('timecreated')['systemtime']))
        # time = datetime.datetime.strptime(soup.find('timecreated')['systemtime'], '%Y-%m-%d %H:%M:%s.%f')

        # print("=========================================")

        if Thistime.hour > 18 or (Thistime.hour == 18 and Thistime.minute > 30 ):
            # print(Thistime)
            # print(timeDetail[1]  + str(Thistime))  # [class 'datetime.datetime']
            if isInitial == True:
                day_start = Thistime.replace(hour=18,minute=30)
                day_end = Thistime
                extraTime = day_end - day_start
                total_time.append(extraTime)
                print(str(Thistime.month) + '월 \t ' + str(Thistime.day) + '일' + '\t~'+ str(day_end) + ' 시간 :\t  ' + str(extraTime))

                isInitial = False

            if Thistime.day != day_start.day :
                isInitial = True
                day_end = Thistime
tt = total_time[0]
for i in range(1,len(total_time)):
    tt = tt + total_time[i]
print(tt)

#
# day = []
# time = []
# extraWork= []
# day_start = datetime.datetime.now()
# day_end = datetime.datetime.now()
# total_time = []

# while True:
#     line = f.readline()
#     if not line:
#         break
#     if line =='\n':
#         pass
#     else:
#         # print(line,end='')
#         linestr = line.split('	')
#         if linestr[0] == '정보' or linestr[0] == '오류' or linestr[0] == '경고':
#             timeDetail = linestr[1].split(' ')
#             target_time = timeDetail[0]+' '+ timeDetail[2]
#             Thistime = datetime.datetime.strptime(target_time, '%Y-%m-%d %H:%M:%S')
#             # print(Thistime)
#             if timeDetail[1] =='오후' and int(timeDetail[2].split(':')[0]) < 12:
#                 Thistime = Thistime + datetime.timedelta(hours=12)
#
#
#             if Thistime.hour > 18 or (Thistime.hour == 18 and Thistime.minute > 30 ):
#                 # print(Thistime)
#                 # print(timeDetail[1]  + str(Thistime))  # [class 'datetime.datetime']
#                 if isInitial == True:
#                     day_start = Thistime.replace(hour=18,minute=30)
#                     day_end = Thistime
#                     extraTime = day_end - day_start
#                     total_time.append(extraTime)
#                     print(str(Thistime.month) + '월 \t ' + str(Thistime.day) + '일' + '\t~'+ str(day_end) + ' 시간 :\t  ' + str(extraTime))
#
#                     isInitial = False
#
#                 if Thistime.day != day_start.day :
#                     isInitial = True
#                     day_end = Thistime
#
# tt = total_time[0]
# for i in range(1,len(total_time)):
#     tt = tt + total_time[i]
# print(tt)
#
#
# f.close()
