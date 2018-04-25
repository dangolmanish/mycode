import random
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

x = int(input('Please enter the length of the number of password you want to generate'))
a = ''.join(random.sample(alpha,x))

print(a)

