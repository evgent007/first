def greet(n,*a):
    s = ' and '.join((n,)+a)
    return 'Hello, '+ s + '!'

s = ('Bob', 'Ann', 'Moe')
print(greet())
