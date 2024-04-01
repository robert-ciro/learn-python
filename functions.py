def is_odd(number):
    return number % 2 != 0


print(is_odd(2))
print(is_odd(3))


# default parameter values
def gree(name="unknown"):
    print("Hello", name)


gree()
