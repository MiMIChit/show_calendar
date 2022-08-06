def getDay(year):
    message="0:Sunday\n1:Monday\n2:Tuesday\n3:Wednesday\n4:Thursday\n5:Friday\n6:Saturday\n"
    day=int(input("Please enter day name of the first day for the year"+str(year)+"\n"+message))
    return day

def getMonthAndYear():
    userInput=input("Please enter month&year in the form month/year")
    list=userInput.split("/")
    return int(list[0]),int(list[1])

def calFirstDay(firstDayOfYear,month,year):
    daysInMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%400==0 or (year%4==0 and year%100!=0):
        daysInMonth[1]=29
    totalDays=0
    for i in range(month-1):
        totalDays+=daysInMonth[i]
    firstDayOfMonth=(firstDayOfYear+totalDays)%7
    days=daysInMonth[month-1]
    return firstDayOfMonth,days

def main():
    dayList=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    month,year=getMonthAndYear()
    day=getDay(year)
    firstDayOfMonth,days=calFirstDay(day,month,year)
    print("First Day:",dayList[firstDayOfMonth])
    print("Month:",month)
    print("Year:",year)
    showCalendar(firstDayOfMonth,days,month,year)

def showCalendar(firstDayOfMonth,daysInMonth,month,year):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    print(months[month-1],year)
    print("Su\tMo\tTu\tWe\tTh\tFr\tSa")
    space="  "
    message=space+"\t"
    count=firstDayOfMonth
    message=message*firstDayOfMonth
    print(message,end="")
    for i in range(1,daysInMonth+1):
        if i<10:
            print(" "+str(i)+"\t",end="")
        else:
            print(str(i)+"\t",end="")
        count+=1
        if count%7==0:
            print()

main()