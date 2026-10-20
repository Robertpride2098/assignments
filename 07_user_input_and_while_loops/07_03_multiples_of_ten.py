# Multiples of ten 
# Robert Pride
# Difficulty 4/10


chosen_car = input('what is your chosen number?:')
yes_or_no = int(chosen_car) % 10
if yes_or_no == 0:
    print(f'{chosen_car} is a multiple of ten.')
else: 
    print(f'{chosen_car} is not a multiple of ten.')