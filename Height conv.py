height = input("Enter the Height's of students: ")   #Input the height's of students seperated by spaces

lst = height.split()    #Splitting the input to convert into a list
print("Entered Height's in feet are ", lst)
sum1 = 0
a = []     #new list to store height in cm
for num in lst:
    sum1 = float(num) * 30.48
    a.append(sum1)
print("Height in cm: ", a)
