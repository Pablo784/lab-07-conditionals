import datetime

# now.hour = int(input("What hour is it? (0-23)"))

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if now.hour <= 5:
    print("It’s early. You should be sleeping!")
elif now.hour <= 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif now.hour <= 9:
    print("Time to go to work.")
elif now.hour <= 12:
    print("You should be working!")
# put all the rest of the conditions here!
else:
    print("You didn’t type an acceptable value! (0-23)")
