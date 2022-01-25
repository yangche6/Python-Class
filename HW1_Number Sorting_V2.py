#creating an empty list
list=[] 

#use for loop to convert string to a list
list=[int(numbers) for numbers in input("Please enter your numbers: ").split()]

print("Your input is: ",list)

#sorting the list
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
             list[i],list[j]=list[j],list[i]

print("Sorted result is: ",list)