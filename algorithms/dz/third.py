def del_repeat_num(list1):
    l2 = []
    for i in list1:
        if i not in l2:
            l2.append(i)
    return l2

def check_l2(l2):
    set_l2 = list(set(l2))
    if del_repeat_num(l2) == set_l2:
        return True
    else:
        return False
    
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 1, 3, 5, 7, 9]
b = del_repeat_num(a)
print(b)
print(check_l2(b))