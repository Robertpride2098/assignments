# deli 
# Robert Pride
# Difficulty 5/10

sandwich_orders = ["tuna", "turkey", "veggie"]
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop(0)
	print(f"I made your {sandwich} sandwich.")
	finished_sandwiches.append(sandwich)

print("The following sandwiches were made:")
for sandwich in finished_sandwiches:
	print(sandwich)



