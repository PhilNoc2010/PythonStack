for i in range(151):
    print(i)

for i in range (5,1001,5):
    print(i)

for i in range(1,101):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 == 0):
        print("Coding")
    else:
        print(i)

sum_total = 0
for i in range(0,500000):
    if (i % 2 == 1):
        sum_total = sum_total + i
print(sum_total)

for i in range(2018,0,-4):
    print(i)

low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num+1):
    if(i % mult == 0):
        print(i)
