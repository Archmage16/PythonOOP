n = input("Write int number: ")
# if n.isdigit() != True:
if not n.isdigit():
    print("It isn't int number")

k = int(input("Write quantity del numbers: "))
if k > len(n):
    print("k is bigger than n")

i = 1
start = 0
while k > 0:
    t = n[start:start + k+1]
    t_max = max(t)
    t_indmax = t.index(t_max)
    if t_indmax > 0:
        t = t[t_indmax:]
        n = n[:start] + t + n[start+k+1:]
    else:
        start += 1

    k -= t_indmax
print(n)