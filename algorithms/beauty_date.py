import datetime

year = int(input("Write a year: "))
year_sum = sum([int(i) for i in str(year)])

beauty_dates = []
for m in range(1, 13):
    for d in range(1,32):
        try:
            date = datetime.date(year, m, d)
            day_month = sum([int(i) for i in str(d)] ) + sum([int(i) for i in str(m)])
            if day_month == year_sum:
                beauty_dates.append(date.strftime("%d-%m-%Y"))
        except ValueError:
            continue
            
print(beauty_dates)