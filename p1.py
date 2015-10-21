# Quiz8
xlist = []
ylist = []
a = int(input("How long would you like your lists to be"))
for i in range(a):
    x = int(input("Give me some number "))
    xlist.append(x)
for i in range(a):
    y = int(input("Give me some numbers "))
    ylist.append(y)
x=0
p=0
for i in range(a):
    p+= int(xlist[x])*int(ylist[x])
    x+=1
print (p)
