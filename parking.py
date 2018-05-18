import pymysql
import datetime

db = pymysql.connect("localhost","root","","carpark" )

numberplate="wpBXX-1414"
locationid = 0
vehical = None
vtypeid=None
lenth = len(numberplate)

now = datetime.datetime.now()
date = str(now)[:10]

if(lenth==10):
    type = numberplate[2]
    print("type ",type)
    if(type=="C" or type=="K" or type=="J"):
        vehical="Car"
        vtypeid = 1
    elif (type=="B"):
        vehical = "Bike"
        vtypeid = 2
    elif(type=="A"):
        vehical = "3while"
        vtypeid = 3
    else:
        print("Invaild Vehical Type")
else:
    print("Wrong Number Plate Detection");

if(vehical != None):

    cursor = db.cursor()

    getLocationSql = "SELECT locationid FROM location WHERE free=1 AND vtypeid= %s LIMIT 1" %(vtypeid)

    try:
       cursor.execute(getLocationSql)
       locationid = cursor.fetchone()
       #print(locationid)
       print("Location ",locationid[0])

       parkingInsertSql = "INSERT INTO parking( numberplate,date,stime, locationid) VALUES ('%s','%s',NOW(), '%d' )" % (numberplate,date,locationid[0])
       cursor.execute(parkingInsertSql)

       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # disconnect from server
    db.close()