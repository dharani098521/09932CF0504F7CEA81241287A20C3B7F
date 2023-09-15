# to find leapyear
year=2000
if(year%400==0)and(year%100==0):
  print("{0}is a leap year".format(year))
elif(year%4==0)and(year%100!=0):
  print("{0}is a leap year".format(year))
  print("{0}is not a leap year".format(year))



year = (int(input()))
if isLeapYear(year):
  print("{} is leap year".format(year))
else:
  print("{} is not leap year".format(year))
