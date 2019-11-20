lista = [1, 4, 7, 8, 9, 13, 15, 18, 22, 35]
target =  35

start = 0
end = len(lista)-1

done = False

while done == False:
    mid = (start+end)//2
    if lista[mid] == target:
        done = True
    
    if lista[mid]>target:
        end = mid -1
    elif lista[mid] < target:
        start = mid + 1


'''

    if start  == end:
        mid = -1
        done = True



    if end-start == 1:
        mid = end
        done = True


        '''


print(mid)