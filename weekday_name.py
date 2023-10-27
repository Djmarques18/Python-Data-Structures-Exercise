def weekday_name(day_of_week):
    days = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednsday', 5: 'thursday', 6: 'friday', 7: 'saturday'}
    if day_of_week >= 1 and day_of_week <= 7:
     if day_of_week in days:
        day_name = days[day_of_week]
        print(day_name)
    else:
        print("INVALID DAY NUMBER!!")
