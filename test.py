# my_list = [1,2, 3, 7, 11]
# it = iter(my_list)

# print(type(it))
# print(it)

# def decor(fn):
#     def wrapper():
#         print("Before the inner")
#         fn()
#         print("After the inner")
#     return wrapper


# @decor
# def hello():
#     return 10


# h1 = hello()


def my_dec(func):

    def wrapper():
        print("*************")
        func()
        print("*************")

    return wrapper

def inner():
    print("say hi")

my_dec(inner)()