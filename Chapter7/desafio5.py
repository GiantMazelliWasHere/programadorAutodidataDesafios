numbers_1 = [8, 19, 148, 4]
numbers_2 = [9, 1, 33, 83]
numbers_3 =[]

for n1 in numbers_1:
    for n2 in numbers_2:
        numbers_3.append(n1 * n2)
    
print(numbers_3)