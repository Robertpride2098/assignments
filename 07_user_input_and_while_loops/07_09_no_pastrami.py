# no pastami 
# Robert Pride
# Difficulty 5/10   

sandwich_orders = ["pastrami", "tuna", "pastrami", "veggie", "pastrami", "turkey"]
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

while sandwich_orders:
	sandwich = sandwich_orders.pop(0)
	print(f"I made your {sandwich} sandwich.")
	finished_sandwiches.append(sandwich)





