def insert_at(orignal, value, index):
    new_list = [0]* (len(orignal)+1)
    i = 0
    while i < index:
        new_list[i] = orignal[i]
        i += 1
    new_list[i] = value
    i += 1
    while i < len(new_list):
        new_list[i] = orignal[i-1]
        i += 1