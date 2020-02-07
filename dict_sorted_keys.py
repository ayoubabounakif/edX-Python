def sort_keys(dict):
    x = list(dict.keys())
    x = sorted(x)
    return x

print(sort_keys({'age': 'Sebastian', 'birthday': 1771, 'name': 'Yohan', 'location': 'bach'}))
print(sort_keys({'cars': 1, 'bikes': 0, 'trucks': 2}))
