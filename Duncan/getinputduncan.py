import requests
import os
from datetime import date
import sys


#Get today number of day
day_today = date.today().strftime("%d").lstrip("0")

#Fetch cookies from Github secrets

try:
    sessionCookie = os.environ["DUNCAN_COOKIE"]
except KeyError:
    print("Please set the environment variable DUNCAN_COOKIE")
    sys.exit(1)

cookies = {'session': sessionCookie}

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day<0 or day>31 or day>int(day_today):
        exit("Day is not valid")
else:
    day = day_today


print(f"Initializing day {day}")

if not os.path.exists(f"Duncan/day{day}"):
    os.mkdir(f"Duncan/day{day}")
    os.chdir(f"Duncan/day{day}")
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies = cookies)
    with open(f"input{day}.txt","w") as f:
        f.write(r.text)