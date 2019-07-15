from Help import *
from datetime import datetime
import time
import cec

while True:
    #let's not do this on weekends
    if(datetime.today().weekday() < 5):
        today = datetime.today()
        tomorrow = today.replace(day=today.day+1, hour=6, minute=0, second=0, microsecond = 0)
        difference = tomorrow-today
        secondstowait = difference.seconds+1
        time.sleep(secondstowait)
        Prep_News()
        today = datetime.today()
        playtime = today.replace(day=today.day, hour=6,minute=45,second=0,microsecond=0)
        difference2 = playtime-today
        secondstowait = difference2.seconds+1
        time.sleep(secondstowait)
        Play_News()
    else:
        time.sleep(10800) #check again in 3 hours
