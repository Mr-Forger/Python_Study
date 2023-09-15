#윤년 구하기 with Function
#TODO1 - 윤년이 맞는 경우 TRUE를 반환하거나, 윤년이 아닌 경우 FALSE 반환
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    print("Not leap year.")

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]
  
  
#🚨 Do NOT change any of the code  below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












