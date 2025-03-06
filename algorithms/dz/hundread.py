import random

def Min_sum_of_Hundread(l1):
    min_sum = sum(l1[:10])
    min_index = 0  
    
    for i in range(len(l1) - 9):
        current_sum = sum(l1[i:i+10])
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i
    
    return min_index, min_sum

l = []
for i in range(1, 100):
    l.append((random.randint(1, 100)))

start_index, min_sum = Min_sum_of_Hundread(l)

print(f"Массив: {l}")
print(f"Минимальная сумма {min_sum} начинается с позиции {start_index}")
print(f"Подмассив: {l[start_index:start_index+10]}")