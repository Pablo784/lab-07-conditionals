usertime = int(input("What hour is it? (0-23)"))

if usertime <= 5:
    print("It’s early. You should be sleeping!")
elif usertime <= 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif usertime <= 9:
    print("Time to go to work.")
elif usertime <= 12:
    print("You should be working!")
# put all the rest of the conditions here!
else:
    print("You didn’t type an acceptable value! (0-23)")
