# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def find_day(month, day, year):
    day_number = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_number]
    return day_name.upper()

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    day_name = find_day(month, day, year)
    print(day_name)
