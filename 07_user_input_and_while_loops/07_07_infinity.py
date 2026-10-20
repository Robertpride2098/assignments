# infity
# Robert Pride
# Difficulty 5/10


loop = True
while loop:
    user_input = input("Would you like to exit?: ")
    if user_input == "yes":
        print("You can not leave the loop.")
    elif user_input == "no":
        print("Continue the loop.")
    elif user_input == "quit":
        loop = False

print("You have exited the loop.")

