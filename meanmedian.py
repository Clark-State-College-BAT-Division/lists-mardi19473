#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# video url: https://youtu.be/VGrRdUunjXg

# RE:Thor's Day
# -Yes! The day names are a combo of Roman celestial names and Norse/other mythology.
# Sun Day, Moon Day, Tyr's Day, Woden (Odin)'s Day, Thor's Day, Frigga's Day, and Saturn's Day.

import statistics

uList = [0, 0, 0, 0, 0]

print("Hello! Enter FIVE (5) integers.")
uList[0] = int(input("First integer: "))
uList[1] = int(input("Second integer: "))
uList[2] = int(input("Third integer: "))
uList[3] = int(input("Fourth integer: "))
uList[4] = int(input("Fifth integer: "))

print(f"You entered {uList}.")

uList.sort()
print(f"Ordered, you entered {uList}.")

uList.sort(reverse=True)
print(f"In reverse, that's {uList}.")

uListMean = statistics.mean(uList)
print(f"The Mean is {uListMean}")

uListMedian = statistics.median(uList)
print(f"The Median is {uListMedian}")