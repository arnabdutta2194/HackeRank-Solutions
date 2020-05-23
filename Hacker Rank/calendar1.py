import calendar
var=input().split()
yr=var[2]
mn=var[0]
day=var[1]

dy=calendar.weekday(int(yr),int(mn),int(day))
if dy == 0:
    print("MONDAY")
elif dy == 1:
    print("TUESDAY")
elif dy == 2:
    print("WEDNESDAY")
elif dy == 3:
    print("THURSDAY")
elif dy == 4:
    print("FRIDAY")
elif dy == 5:
    print("SATURDAY")
elif dy == 6:
    print("SUNDAY")