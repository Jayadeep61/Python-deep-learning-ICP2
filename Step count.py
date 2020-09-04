numb = int(input("Enter a number: "))
count = 0

while numb != 0:
    a = numb % 2
    if a == 0:
        numb = numb / 2
        count = count + 1
    else:
        numb = numb - 1
        count = count + 1

print("No. of steps taken: ", count)