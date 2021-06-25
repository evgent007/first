def count_all(it):
    s = {}
    for i in it:
        n = it.count(i)
        s[i] = n
    return s
print(count_all([]))
