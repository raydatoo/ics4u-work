
'''
time = 5

def count_score(n):
    if len(n) == 0:
        return 0
    elif n[0].collected == True:
        return time*n[0].collection_bonus + count_score(n[1:]) 
    else:
        return 0 + count_score(n[1:])


class Coin():
    def __init__(self, collection_bonus):
        self.collection_bonus = collection_bonus
        self.collected = False


a = Coin(5)
b = Coin(3)
c = Coin(6)
d = Coin(5)

liy = [a,b,c,d]

a.collected = True


print(count_score(liy))


'''



