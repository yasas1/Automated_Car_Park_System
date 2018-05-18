import pymysql
import time
import datetime

db = pymysql.connect("localhost","root","","carpark" )

parkingid=13

etime=time.strftime("%H:%M:%S")

print(etime)

cursor = db.cursor()

getStimeSql = "SELECT stime FROM parking WHERE parkingid=%d " %(parkingid)

try:
    cursor.execute(getStimeSql)
    stimeresult = cursor.fetchone()

    stime=str(stimeresult[0])
    print(stime)
    time1 = datetime.datetime.strptime(stime, '%H:%M:%S')
    print(time1)
    time2 = datetime.datetime.strptime(etime, '%H:%M:%S')
    print(time2)
    print(str(time2 - time1))


    parkedtime = datetime.datetime.strptime(str(time2 - time1) , '%H:%M:%S')
    print(parkedtime)

    price = 0

    if parkedtime.time() >= datetime.time(8,00,0):
        price = 500
    elif parkedtime.time() >= datetime.time(4,0,0):
        price = 300
    elif parkedtime.time() >= datetime.time(2,0,0):
        price = 200
    elif parkedtime.time() >= datetime.time(1,0,0):
        price = 100
    else:
        price = 50

    print(parkedtime.time())
    print(time1.time())
    print(time2.time())

    updateEtime = "UPDATE parking SET etime='%s' , totalprice=%d WHERE parkingid=%d " %(etime,price,parkingid)

    cursor.execute(updateEtime)

    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

db.close()