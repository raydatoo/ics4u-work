def get_shopping_list(inventory, minimum_stock):
    needed = []
    for invkey, invvalue in inventory.items():
       current_fruit = invkey
       qty_in_fridge = invvalue
       for stockkey, stockvalue in minimum_stock.items():
           if stockkey == current_fruit: 
               qty_needed = stockvalue
               if qty_in_fridge<qty_needed:
                   needed.append(stockkey)
    return needed
print(get_shopping_list({"apples": 5, "pears": 7, "plums": 11, "kiwi" : 3, "pineapple": 1, "watermelon": 2, "eggs": 8}, {"apples": 15, "pears": 10, "plums": 5, "watermelon": 1, "kiwi": 5, "eggs":12, "pineapple": 3}))



what the black is a csv 

