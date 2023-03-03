def add_time(start, duration, stday=None):
    days = 0
    st = start.split(" ")
    hour, minute = st[0].split(":")
    duhr, dumin = duration.split(":")
    hour, minute, duhr, dumin = int(hour), int(minute), int(duhr), int(dumin)
    newhr = int(hour) + int(duhr)
    newmin = int(minute) + int(dumin)
    dayto = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
    today = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    if newmin > 59:
        newmin -= 60
        if newmin < 10:
            newmin = "%02d" % newmin
        newhr += 1
    while newhr > 12:
        if newhr > 12 and st[1] == "AM":
            st[1] = "PM"
            newhr -= 12
        if newhr > 12 and st[1] == "PM":
            st[1] = "AM"
            newhr -= 12
            days += 1

    if hour < 12 and newhr == 12:
        if st[1] == "AM":
            st[1] = "PM"
        else:
            st[1] = "AM"
            days += 1

    print(f"{newhr}:{newmin} {st[1]}", end="")
    if stday != None:
        stday = stday.lower()
        a = dayto.get(stday)
        a += days
        a = a % 7
        day = today.get(a)
        print(f", {day}", end="")
    if days > 0:
        if days == 1:
            print(f" (nextday)", end="")
        else:
            print(f" ({days} days later)", end="")
    print("\n")


add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")

