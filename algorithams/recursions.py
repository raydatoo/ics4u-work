def count_ears(num):
    if num == 0:
        return 0
    else:
        return 2 + count_ears(num-1)





def count_triangle(num):
    if num == 0:
        return 0
    else: 
        return num + count_triangle(num-1)






def count_ints(n):

    if n == 0:
        return 0
    else: 
        return n%10 + count_ints(n//10)


print(count_ints(7860))







def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(2))


def new_bunnies(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return 3 + new_bunnies(n-1)
    elif n%2 == 1:
        return 2 + new_bunnies(n-1)


print(new_bunnies(2))





def count_7(n):
    if n == 0:
        return 0
    elif n%10 == 7:
        return 1 + count_7(n//10)
    else:
        return count_7(n//10)


print(count_7(7346854736783467846782))




def count_8(n):
    if n == 0:
        return 0
    elif n%100 == 88:
        return 2 + count_8(n//10)
    elif n%10 == 8:
        return 1 + count_8(n//10)
    else:
        return count_8(n//10)


print(count_8(9934588))



