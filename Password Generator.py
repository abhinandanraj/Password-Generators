import random

char = 'qwui5o@p1a&sdfg4hk3lz2xnmj#ey$%*_06t7r8cvb9'

password = []

rand = random.randint(5,15)

for i in range(1, rand):

    index = random.randint(1, 43)

    password.append(char[index])

password = ''.join(password)

print('Your password is : ' + password)
