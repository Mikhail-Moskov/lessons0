import random
number = random.choice(range(3,20))
password = []
for a in range(2, number):
    for b in range(1,a):
        if number % (a+b) == 0:
            if a == b:
                continue
            elif a < b:
                password.append([a, b])
            else:
                password.append([b, a])
password.sort()
print(number)
print(*password)