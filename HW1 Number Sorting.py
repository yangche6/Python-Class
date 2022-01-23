#creating an empty list
list=[] 

#use for loop to convert string to a list
list=[int(numbers) for numbers in input("Please enter your numbers: ").split()]

print("Your input is: ",list)

#sorting the list
list.sort()

print("Sorted result is: ",list)