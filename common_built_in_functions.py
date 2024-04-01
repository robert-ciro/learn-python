print(abs(-1))  # 1

print(all([1, 1, 1]))  # true
print(all([1, 1, None]))  # false
print(all((0, True, False)))  # false
print(all({0, 1, 0}))  # false
print("all({1, 1, 1} =", all({1, 1, 1}))  # true


print("any([False, True, False]) =", any([False, True, False]))  # true
print("any([False, False, False]) = ", any([False, False, False]))  # false
print("any([]) =", any([]))  # false

print("chr(122) =", chr(122))  # Unicode code point 122 return 'z'


print("divmod(10, 6) =", divmod(10, 6))  # (1, 4) (x // y, x % y)

print(id(5 + 6))  # memory address 140709315234552


def double(number):
    return number * 2


for number in map(double, [1, 2, 3, 4]):
    print(number)

print("max(1, 2, 3, 4) =", max(1, 2, 3, 4))  # 4
print("max([1, 2, 3, 4]) =", max([1, 2, 3, 4]))  # 4

print("min(1, 2, 3, 4) =", min(1, 2, 3, 4))  # 1
print("min([1, 2, 3, 4]) =", min([1, 2, 3, 4]))  # 1

animals = iter(["Dog", "Cat"])
print("next(['Dog', 'Cat'])", next(animals))  # Dog
print("next(['Dog', 'Cat'])", next(animals))  # Cat


print("pow(4, 2) =", pow(4, 2))  # 16

print("pow(2, 3, 5) =", pow(2, 3, 5))  # (2^3) % 5 = 3

print("range(1, 10):")
_1_to_9 = range(1, 10)

for number in _1_to_9:
    print(number)

reversed_numbers = reversed([1, 2, 3])

print("Reversed numbered of [1, 2, 3] ")
for number in reversed_numbers:
    print(number)


print("round(2.4) =", round(2.4))  # 2
print("sorted([2, 1, 4, 3])=", sorted([2, 1, 4, 3]))  # [1,2,3,4]
print("sum([1, 2])  =", sum([1, 2]))  # 3
