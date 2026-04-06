#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken 
#You entered a total of 62 characters

foodList = ["firstfood", "secondfood", "thirdfood", "fourthfood", "fifthfood"]

print("What are your top FIVE favorite foods?")
foodList[0] = input("First favorite food: ")
foodList[1] = input("Second favorite food: ")
foodList[2] = input("Third favorite food: ")
foodList[3] = input("Fourth favorite food: ")
foodList[4] = input("Fifth favorite food: ")

print("Your favorites foods are:")
print(", ".join(foodList))

#Using LEN with comprehension to count length of each word and then combine into one sum.
#print(f"Total characters entered: {sum(len(i) for i in foodList)}")

#Using REPLACE to remove middle spaces for more accurate character count.
foodList2 = [item.replace(" ", "") for item in foodList]
print(f"Total characters entered: {sum(len(i) for i in foodList2)}")
