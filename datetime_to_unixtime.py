#sudo pip install --no-deps astropy

import time
import datetime
from datetime import date
from time import mktime
import numpy

def main():
  rows = 17
  columns = 2
  datetimelist = numpy.zeros((rows, columns))
  #Date   UTT(Trigger) ## UTT???
  datetimelist = [["2014,12,21","8:07:10"],
   ["2014,12,21","21:31:48"],
   ["2014,12,22","7:08:55"],
   ["2014,12,22","16:34:30"],
   ["2014,12,23","5:45:37"],
   ["2014,12,25","23:01:13"],
   ["2014,12,26","21:07:24"],
   ["2014,12,29","11:48:59"],
   ["2014,12,29","21:52:10"],
   ["2014,12,30","3:24:22"],
   ["2014,12,30","20:00:25"],
   ["2014,12,30","20:54:05"],
   ["2015,01,01","6:28:53"],
   ["2015,01,01","15:23:34"],
   ["2015,01,03","20:02:18"],
   ["2015,01,05","6:10:00"],
   ["2015,01,06","22:05:56"]]

  print "GRB times in unixtime"

  for i in range(rows):
    stringdate = datetimelist[i][0]
    #print stringdate
    stringtime = datetimelist[i][1]
    #print stringtime
    unixtime = time.mktime(datetime.datetime.strptime(stringdate, "%Y,%m,%d").timetuple())
    #print unixtime
    timeseconds = sum(int(x) * 60 ** i for i,x in enumerate(reversed(stringtime.split(":"))))
    unixtime = unixtime + timeseconds
    print unixtime

main()
