#coding=utf8
import datetime
while True:
    company=raw_input('请输入您公司的全称\n').strip()
    if len(company)< 1:
        continue
    break
while True:
    intime=raw_input("请输入您的入职日期,例如2017-2-3\n").strip()
    if (len(intime) < 8) or (intime.count("-")!=2):
        continue
    break
iyear=intime.split('-')[0]
imonth=intime.split('-')[1]
iday=intime.split('-')[2]

starttime=datetime.datetime(int(iyear),int(imonth),int(iday))
endtime=datetime.datetime.now()
dayed=(endtime-starttime).days
if (dayed//365) >=1:
    yeared=dayed//365
    dayed=dayed%365
    print("您已经为%s服务%d年%d天") % (company,yeared,dayed)
else:
    print("您已经为%s服务了%d天") % (company,dayed)

