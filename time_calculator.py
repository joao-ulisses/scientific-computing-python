def add_time(start, duration, startDay=''):
    startDayCount = 0
    if startDay != '':
        startDay = startDay.lower()
        days = {
            'sunday': 0,
            'monday': 1,
            'tuesday': 2,
            'wednesday': 3,
            'thursday': 4,
            'friday': 5,
            'saturday': 6
        }
        startDayCount = days[startDay]

    nextDayCount = 0
    hoursToAdd, minutesToAdd = duration.split(":")
    if int(minutesToAdd) >= 60:
        pass        

    hoursNow, minutesNow = start.split(":")
    minutesNow, midDayNow = minutesNow.split()
    hoursNow = int(hoursNow)
    hoursToAdd = int(hoursToAdd)

    minutesNow = int(minutesNow)
    minutesNow += int(minutesToAdd)
    if minutesNow >= 60:
        hoursToAdd += minutesNow // 60
        minutesNow = minutesNow % 60    

    for i in range(1, hoursToAdd+1):
        hoursNow += 1
        if hoursNow > 12:
            hoursNow = 1
        if hoursNow > 11:
            if midDayNow == "PM":
                nextDayCount += 1
                if startDayCount == 6:
                    startDayCount = 0
                else:
                    startDayCount += 1
                midDayNow = "AM"
            else:
                midDayNow = "PM"

    
    if minutesNow < 10:
        minutesNow = '0' + str(minutesNow)
    new_time = f'{hoursNow}:{minutesNow} {midDayNow}'

    
    if startDay != '':
        dateNow = [key for key, value in days.items() if value == startDayCount][0]
        dateNow = dateNow[0].upper() + dateNow[1:]
        new_time += f', {dateNow}'
    
    if nextDayCount > 1:
        new_time += f' ({nextDayCount} days later)'
    elif nextDayCount == 1:
        new_time += ' (next day)'
    
    return new_time

print(add_time('3:30 PM', '2:12', 'Monday'))