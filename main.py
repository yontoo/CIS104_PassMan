#PassMan
import random
import string
password_list = []

print('''
Password Manager
----------------------------
"new" - Create new password.
"find" - Look up a password.
''')
def new_pass():
    website = input("Website name: ")
    username = input("Username: ")
    password = input("Password: ")
    if (password == "random"):
        pass_length = int(input('Password length: '))
        random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pass_length))
        print(f'Random password: {random_password}')
        password = random_password
    website_entry = dict([("website", website), ("username", username), ("password", password)])
    password_list.append(website_entry)
    print(password_list)

# def find():
#     website = input("Which website?: ")
#     for entry in password_list:
#         if found_website == entry.get['website']:
#             print(entry['username'])
#             print(entry['password'])
#         else:
#             print("Website doesn't exist")
    


#input info to be saved
while True:
    user_choice = input(">")

    if (user_choice == 'new'):
        new_pass()
    elif (user_choice = 'find'):
        find()
    else:
        continue
    


    #print(website + "\n" + username + "\n" + password)