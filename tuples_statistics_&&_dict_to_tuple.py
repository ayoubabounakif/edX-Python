# Program to calculate the mean and the median of a tuple
def _(tuple):
    import numpy as np
    mean = sum(tuple) / len(tuple)
    median = np.median(np.array(tuple))
    return (mean, median)


print(_((600, 470, 170, 170, 430, 300),))
# Program that converts a dictionary to a tuple


"""def ___(dict):
    keys=tuple(dict.keys())
    values=tuple(dict.values())
    return keys, values


# print(___({1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}))"""
