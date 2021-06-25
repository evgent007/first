def make_user(name,age):
    return {'name':name,'age':age}
def format_user(name):
    return '{},{}'.format(name['name'],name['age'])
bob = make_user('bob',25)
print(bob)
print(format_user(bob))
print(bob['age'])
