# Movie tickets 
# Robert Pride
# Difficulty 3/10   

tickets = True
while tickets: 
    age_of_customer = input('What is your age? ')
    if age_of_customer == 'quit':
        tickets = False

    elif int(age_of_customer) < 3:
        print('Your ticket is free.')
    elif int(age_of_customer) < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')