# Program is to find the day after 10,20 or after nth days from now 
# Considering as 1 day is monday,2 day is tuesday and so on... upto 7th day is Sunday

# Suppose today is Tuesday then what would be the day after 100 days....






# Function to return day name by accepting integer value woks as a switch case 
def week(i):
    switcher={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday', 4:'Thursday',5:'Friday',6:'Saturday'}
    return switcher.get(i,"Invalid day of week")





today=eval(input("Enter todays's number as per above consideration's in manual "))
days=eval(input("After how many days you want to check.. "))
upcoming_day= (today+days) % 7
print("Upcoming Day :: ",week(upcoming_day))