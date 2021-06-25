def length_of_last_word(s):
    
    c = [' ','\n','\t']
    n = 0
    for i in s[::-1]:
        print('i =',i,'n=',n)
        if i in c :
            print('DA')
            if n > 0:
                return n
            else:    
                continue
        else:
            n += 1
    return n

print(length_of_last_word(' \t\n'))

print('hello\t\nworld'.split())
