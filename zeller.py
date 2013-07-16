first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
print "Enter your date of birth: "
mon = int(raw_input("Month? Enter a number between 1-12: "))
day = (raw_input("Day? "))
year = (raw_input("Year? "))


A = mon - 2
B = int(day)
C = int(year[2:4])
D = int(year[0:2])
if mon==1:
    A = 11
    C = C-1
elif mon==2:
    A = 12
    C = C-1

W = (13*A - 1)/5
X = C/4
Y = D/4
Z = W + X + Y + B + C - 2*D
R = Z%7
if R == 0:
    day_of_week = "Sunday"
elif R == 1:
    day_of_week = "Monday"
elif R == 2:
    day_of_week = "Tuesday"
elif R == 3:
    day_of_week = "Wednesday"
elif R == 4:
    day_of_week = "Thursday"
elif R == 5:
    day_of_week = "Friday"
elif R == 6:
    day_of_week = "Saturday"

print first_name, last_name, "was born on", str(day)+"/"+str(mon)+"/"+str(year)+",", day_of_week+"."



