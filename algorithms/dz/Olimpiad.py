#просил помощь у нейросети так, как не смог понять алгоритм


a = int(input("Введите количество 9-классников: "))
b = int(input("Введите количество 10-классников: "))
c = int(input("Введите количество 11-классников: "))

freq = {9: a, 10: b, 11: c}

result = []
last = None  

while freq:
    candidate = None       
    candidate_count = -1   

    for grade in list(freq.keys()):
        if grade == last:
            continue
        if freq[grade] > candidate_count:
            candidate = grade
            candidate_count = freq[grade]

    if candidate is None:
        break

    result.append(candidate)
    last = candidate

    freq[candidate] -= 1
    if freq[candidate] == 0:
        del freq[candidate]

print("Упорядоченный список:", result)
print("Количество участников:", len(result))

    