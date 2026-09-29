# I think it is diffuculty of 7/10


current_users = ['admin', 'colton', 'desai', 'robert', 'james']
new_users = ['admin', 'colton', 'desai', 'robert', 'james', 'michael', 'sarah', 'emily']

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, {new_user}. That username is already taken.")
    else:
        print(f"Great! {new_user} is available.")
