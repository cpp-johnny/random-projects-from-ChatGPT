import calendar

# Create a plain text calendar
c  = calendar.TextCalendar(calendar.SUNDAY)

str = c.formatmonth(2022, 12, 0, 0) # year = 2022, month = 12 (Dec)

print(str)
