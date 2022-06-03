import random
print('Welcome to our Password Generator')
chars = 'Odero@98%'
number = input('Entre how many paswords you want to generate: ')
number = int(number)
length = input('Entre the length of characters you want inside your password: ')
length = int(length)

print('\n Here are your passwords:')
for pwd in range (number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)