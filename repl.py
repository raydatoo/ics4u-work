def check_and_update_high_score(current_score: int):
	with open("high_score.txt", "r") as fole:
        bean = int(fole.read())
    if bean < current_score 
        with open("high_score.txt", "w") as file:
		    file.write(str(current_score))
		
	return None
		
		
		
print(check_and_update_high_score(45))