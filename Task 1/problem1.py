num = []

d = input().split()

for i in d:
    num.append(int(i))

unq_num = []

for j in num:
    if j not in unq_num:
        unq_num.append(j)

if len(unq_num) < 2:
    print(-1)
else:
    max1 = unq_num[0]

    for j in unq_num:
        if j > max1:
            max1 = j

  
    unq_num.remove(max1)

   
    max2 = unq_num[0]

    for j in unq_num:
        if j > max2:
            max2 = j

    print(max2)
