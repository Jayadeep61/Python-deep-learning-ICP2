myfile = open("original.txt")    #Opening the file for reading
content = myfile.read()          #Performing the read operation
print(content)
a = content.split()              #Splitting the file content to make it as a list
#a.sort()
c = []                           #New list
for i in a:                      #Checking each item and calculating the count value
    if i not in c:
        b = a.count(i)
        print(i, b)
        c.append(i)