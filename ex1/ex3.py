def isLeapYear(year):
    return year%4==0 and (year%100!=0 or year%400==0)

year = int(input("Please give a year:\n"))
if isLeapYear(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")