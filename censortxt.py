from better_profanity import profanity 

file = open(r"ProfaneText.txt", "r")

censoredFile = open("CensoredText.txt", "w")

uncensored = file.read()

censoredText = profanity.censor(uncensored)
if profanity.contains_profanity(uncensored):
	print("WARNING: CONTAINS PROFANITY")
	

print(censoredText)

censoredFile.write(censoredText)

file.close()
censoredFile.close()