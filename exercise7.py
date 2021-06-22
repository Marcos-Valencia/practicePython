print('start')

a = [1,4,9,16,25,36,49,64,81,100]
even_list =[]
for len in a:
    temp = len % 2
    if temp == 0:
        even_list.append(len)
    else:
        print(len, " item is not even")
print(even_list, " These are all the even numbers")
