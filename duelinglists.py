#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
#Player Two = 3,8,5,5,8,1,4,7,4,7
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

random.seed()

p1WinCount = 0
p2WinCount = 0

listP1 = [random.randint(1, 50) for _ in range(10)]
listP2 = [random.randint(1, 50) for _ in range(10)]

#if listP1[0] > listP2[0]:
#    p1WinCount += 1
#elif listP1[0] < listP2[0]:
#    p2WinCount += 1
#else:
#    pass
#repeat for 0-9 on list
#Switch to ZIP and compare?
for item1, item2 in zip(listP1, listP2):
    if item1 > item2:
        p1WinCount += 1
    elif item1 < item2:
        p2WinCount += 1
    else:
        pass


#Using comprehension to print int as str, add commas between numbers.
print(f"Player One's numbers are {", ".join([str(n) for n in listP1])}.")
print(f"Player Two's numbers are {", ".join([str(n) for n in listP2])}.")

print(f"Player One won {p1WinCount} times.")
print(f"Player Two won {p2WinCount} times.")

p1High = max(listP1)
#p1HighFirst = listP1.index(p1High)
p2High = max(listP2)
#p2HighFirst = listP2.index(p2High)
p1Low = min(listP1)
#p1LowFirst = listP1.index(p1Low)
p2Low = min(listP2)
#p2LowFirst = listP2.index(p2Low)

#print(f"Player One's highest number was {p1High} at index position {listP1.index(p1HighFirst)}.")
#print(f"Player Two's highest number was {p2High} at index position {listP2.index(p2HighFirst)}.")
#print(f"Player One's lowest number was {p1Low} at index position {listP1.index(p1LowFirst)}.")
#print(f"Player Two's lowest number was {p2Low} at index position {listP2.index(p2LowFirst)}.")

#add code for only using first occurrence in list
#p1LowFirst = listP1.index(p1Low)
#print(f"P1 first low index is {p1LowFirst}.")

#Was all unneccesary because MAX/MIN returns first instance, and can be used to find index of that occurence. -.-;;


print(f"Player One's highest number was {p1High} at index position {listP1.index(p1High)}.")
print(f"Player Two's highest number was {p2High} at index position {listP2.index(p2High)}.")
print(f"Player One's lowest number was {p1Low} at index position {listP1.index(p1Low)}.")
print(f"Player Two's lowest number was {p2Low} at index position {listP2.index(p2Low)}.")