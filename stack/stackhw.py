s = input("Write some brackets: ")

Stack = []
is_work = True

for sym in s:
    if s[-1] != ';':
        is_work = False
        break
    if sym in '({[':
        Stack.append(sym)
    elif sym in ')}]':
        if not Stack:
            is_work = False
            break
        open_br = Stack.pop()
    
        if open_br == "(" and sym == ')':
            continue 
        if open_br == "[" and sym == ']':
            continue  
        if open_br == "{" and sym == '}':
            continue  
        
        is_work = False
        break

if is_work and len(Stack) == 0:
    print("You write it correctly!")
else:
    print("You write incorrectly!")