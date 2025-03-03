def decorator_strong(func):
    def strong():
        return "<strong>"+ func() +"</strong>"
    return strong
        
def decorator_i(func):
    # print("we are in decorator_i")
    def italic():
        # print("we are in italic")
        res = func()
        # print("we are leaving italic")
        return "<i>" + res + "</i>"
    # print("we are leaving decorator_i")
    return italic
    

@decorator_strong
@decorator_i
def input_str() -> str:
    s = input("Write a string: ")
    return s

k = input_str()
print(k)



# def f():
#     return "Hello world!"
# print(f())
# print(f)




