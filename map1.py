my_pets = ['alfred', 'tabitha', 'william', 'arla']

l = ['rrrrr','ggggg','kkkkk','iiiii']
uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas,1))

print(result)
