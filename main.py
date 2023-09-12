def checkLeap(year):
  if((year % 400 ==0) or
     (year % 100 !=0) and
     (year % 4 ==0)):
    print(" given year a leap year")
  else:
    print(" given year is not a leap year")
year=int(input("enter the number"))
checkLeap(year)
    
        