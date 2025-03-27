import calendar

def months():
    months = list(calendar.month_name)[1:] 
    for month in months:
        print(month)

if __name__ == "__main__":
    months()
