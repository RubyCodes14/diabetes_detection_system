
import time
#import time, datetime, calendar

class Timestamp():         #Returns the time a file was created as string, to append to a file name
    def __init__(self):
        self.epochTime = time.gmtime(time.time())
        #print(self.epochTime)
        
    def timestamp(self):
        concat_Time, unit_Time = "", ""
        for i in range(6):
            if i != 3:
                unit_Time = str(self.epochTime[i])
            else:
                unit_Time = str(int(self.epochTime[3]) + 1)
                
            if len(unit_Time) == 1:
                unit_Time = "0" + unit_Time
            concat_Time += unit_Time
            
        else:
            concat_Time = [concat_Time[:4], concat_Time[4:6], concat_Time[6:8],
                           concat_Time[8:10], concat_Time[10:12], concat_Time[12:14]]
            
        return concat_Time


#ts = Timestamp()
#print(ts.timestamp())





'''

week = datetime.date(year, month, day)
weekday = week.strftime("%A")

#sample below
print("|\tYour were born on", weekday, suffix(day), str(calendar.month_name[month]) + ",", year, "|")
def suffix(number):
    no = str(number)
    if int(no[-1]) in [i for i in range(4, 21)]:
        suf = "th"
    elif no[-1] == "1": # or len(str(number)) == 2:
        suf = "st"
    elif no[-1] == "2":
        suf = "nd"
    elif no[-1] == "3":
        suf = "rd"
    else:
        suf = ""
    number = str(number) + suf
    return number
    
'''

