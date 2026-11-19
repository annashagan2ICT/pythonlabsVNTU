lista = {'x': 1, 'y': 2, 'z': 3}
listb = {'w': 10, 'x': 11, 'y': 2}

common_keys = lista.keys() & listb.keys()
print(" ".join(common_keys))