from random import randint
# In this code, I thought 3x3 matrix as 3 individual lists and I merged them at the and by using zip() method.
list1 = [0, 0, 0] # I placed three 0's to indicate the length of the list, I'll changed them with random prime values later.
for i in range(3):
    flag = 1  # this is defined to check whether a number is prime or not
    while flag != 0:  # continue until the number is place into the matrix
        a = randint(2, 100) # generating random number a to place into the matrix
        if a == 1 or a == 0:
            while a == 1 or a == 0:
                a = randint(2, 100)
        j = 2  # least prime number is equal to 2, so we start from 2
        while j <= a // 2:  # a number cannot be divided by a number which is larger than its half value
            if a % j == 0 :  # checking whether the number can be divided by numbers which are less than its half value or not
                flag = 1  # if the number can be divided by one of the value of i, then it means that this number is not prime
                break  # no need to continue to the loop since we already found out the number is not prime when the code entered to the if clause
            else:
                flag = 0
                j += 1
        if flag != 1:
            list1[i] = a
            break

list2 = [0, 0, 0] # I placed three 0's to indicate the length of the list, I'll changed them with random prime values later.
for i in range(3):
    flag = 1  # this is defined to check whether a number is prime or not
    while flag != 0:  # continue until the number is place into the matrix
        a = randint(2, 100) # generating random number a to place into the matrix
        if a == 1 or a == 0:
            while a == 1 or a == 0:
                a = randint(2, 100)
        j = 2  # least prime number is equal to 2, so we start from 2
        while j <= a // 2:  # a number cannot be divided by a number which is larger than its half value
            if a % j == 0 :  # checking whether the number can be divided by numbers which are less than its half value or not
                flag = 1  # if the number can be divided by one of the value of i, then it means that this number is not prime
                break  # no need to continue to the loop since we already found out the number is not prime when the code entered to the if clause
            else:
                flag = 0
                j += 1
        if flag != 1:
            list2[i] = a
            break

list3 = [0, 0, 0]  # I placed three 0's to indicate the length of the list, I'll changed them with random prime values later.
for i in range(3):
    flag = 1  # this is defined to check whether a number is prime or not
    while flag != 0:  # continue until the number is place into the matrix
        a = randint(2, 100)  # generating random number a to place into the matrix
        if a == 1 or a == 0:
            while a == 1 or a == 0:
                a = randint(2, 100)
        j = 2  # least prime number is equal to 2, so we start from 2
        while j <= a // 2:  # a number cannot be divided by a number which is larger than its half value
            if a % j == 0:  # checking whether the number can be divided by numbers which are less than its half value or not
                flag = 1  # if the number can be divided by one of the value of i, then it means that this number is not prime
                break  # no need to continue to the loop since we already found out the number is not prime when the code entered to the if clause
            else:
                flag = 0
                j += 1
        if flag != 1:
            list3[i] = a
            break
print(list(zip(list1, list2, list3)))
