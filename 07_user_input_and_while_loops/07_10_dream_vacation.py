# Dream vacation
# robert pride
# diffuculty 5/10

responses = {}

polling = True
while polling:
	name = input("What is your name? ")
	destination = input(
		"If you could visit one place in the world, where would you go? "
	)
	responses[name] = destination

	another_response = input("Would you like to let someone else respond? (yes/no) ")
	if another_response.lower() == "no":
		polling = False
else:
    print("\n--- Dream Vacation Poll Results ---")
for name, destination in responses.items():
	print(f"{name} would like to visit {destination}.")
