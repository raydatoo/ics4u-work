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


#print(count_ints(7860))







def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#print(fibonacci(0))


def new_bunnies(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return 3 + new_bunnies(n-1)
    elif n%2 == 1:
        return 2 + new_bunnies(n-1)


#print(new_bunnies(2))





def count_7(n):
    if n == 0:
        return 0
    elif n%10 == 7:
        return 1 + count_7(n//10)
    else:
        return count_7(n//10)


#print(count_7(7346854736783467846782))




def count_8(n):
    if n == 0:
        return 0
    elif n%100 == 88:
        return 2 + count_8(n//10)
    elif n%10 == 8:
        return 1 + count_8(n//10)
    else:
        return count_8(n//10)


#print(count_8(9934588))


def count_abc(n):
    if len(n) <= 2:
        return 0
    elif n[:3] == "abc" or n[:3] == "aba":
        return 1 + count_abc(n[1:])
    else:
        return count_abc(n[1:])




#print(count_abc("heehdjhabahdudabc"))



def count_x(string):
    if len(string) == 0:
        return 0
    elif string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return 0 + count_x(string[1:])

#print(count_x("xxxxfftxxxtrdtrxdxfdxdfxdxxxtfxftxfx"))




def changepi(n):
    if len(n) == 0:
        return n
    if n[0:2] == "pi":
        return "3.14" + changepi(n[2:])
    else:
        return n[0] + changepi(n[1:])


#print(changepi("pi4ygrygpirnrpihellpi"))



def count_hi(n):
    if len(n) == 0:
        return 0
    elif n[0] == "x":
        return 0 + count_hi(n[2:])
    elif n[0:2] == "hi":
        return 1 + count_hi(n[1:])
    
    else:
        return 0 + count_hi(n[1:])


#print(count_hi("hihithhihihisdvgsdhisdgvdshiewhi"))

def count_11(n):
    if len(n) == 0:
        return 0
    elif n[-1] == 11:
        return 1 + count_11(n[:-1])
    else:
        return 0 + count_11(n[:-1])
    
#print(count_11([2,3,453,4,11,3,4,11,3241,11]))


def string_clean(n):
    if len(n) == 1:
        return n
    elif n[0] == n[1]:
        return string_clean(n[1:])
    else:
        return n[0] + string_clean(n[1:])


#print(string_clean("hhhhheeeelllooooooooo"))



def no_x(n):
    if len(n) == 0:
        return n
    elif n[0] == "x":
        return no_x(n[1:])
    else:
        return n[0] + no_x(n[1:])


print(no_x("xhexdxjbwxxehbshdxxxxjxwbx"))


def pairstar(n):
    if len(n) == 1:
        return n
    elif n[0] == n[1]:
        return n [0] + "*" + pairstar(n[1:])
    else:
        return n [0] + pairstar(n[1:])

#print(pairstar("aabdhdbhdgfvsssaa"))



def allstar(n):
    if len(n) == 1:
        return n
    else:
        return n[0] + "*" + allstar(n[1:])



print(allstar("dsugsauydg"))