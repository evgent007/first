import itertools

def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    #return list(children)
    return list(itertools.chain(*children))
l = [1, [3, 2], 3,[ 5,[], 130] ,[1, [550, 10]]]
print(remove_first_level(l))
