def prime_first(num):
    flag = 0
    i = 2 #since a number cannot be divided by 0 and prime numbers can be divided by 1, i starts from 1
    if num == 0 or num == 1:
        flag = 1
    while i <= num//2:
        if num % i == 0 or num == 0 or num == 1:
            flag = 1
        i = i+1
    if flag == 0:
        print(num)


def prime_second(num):
    flag = 0
    i = 2#since a number cannot be divided by 0 and prime numbers can be divided by 1, i starts from 1

    while i <= num // 2:
        if num % i == 0 or num == 0 or num == 1:
            flag = 1
        i = i + 1
    if flag == 0:
        print(num)


for i in range(1000):
    if i < 500:
        prime_first(i)
    elif 500 <= i < 1000:
        prime_second(i)
