def min_operations(target):
    queue = [(1, 0)]  
    v = set() 

    while queue:
        num, steps = queue.pop(0) 

        if num == target:
            return steps  
        if num > target:
            continue  

        next_numbers = [num * 2, 
            int(str(num) + "1"),
            int(str(num) + "3"),
            int(str(num) + "5"),
            int(str(num) + "7"),
            int(str(num) + "9"),
        ]

        for next_val in next_numbers:
            if next_val not in v:
                v.add(next_val)
                queue.append((next_val, steps + 1))

    return -1 

target = int(input("Введите число: "))
print(min_operations(target))
