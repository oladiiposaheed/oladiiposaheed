a, b = 0, 1
Sum = 0
while b < 50:
    print(b)
    a, b = b, a + b
print('***************')
print('The sum of the first 50 fibonacci sequence = {}'.format(a+b))