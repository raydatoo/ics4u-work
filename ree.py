import json



with open("ree.json", "r") as f:
    player = json.load(f)

print(player["points"])

player["points"] += 50


'''

with open("ree.json", "w") as f:
    player = json.dump(player, f)

    '''