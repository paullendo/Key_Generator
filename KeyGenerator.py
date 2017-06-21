from random import randint

generator = [1]
digits = 1
number = int(input("Number of digits in key?: "))
key = str(1)

while digits < number:
    add = randint(0, 9)
    generator.append(add)
    digits += 1
    key += str(generator[-1])

print(key)