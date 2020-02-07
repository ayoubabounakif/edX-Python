from functools import reduce

def prod(x,y,z):
    nums = x, y, z
    nums_product = reduce( (lambda x, y: x * y), nums)
    return nums_product

print (prod(4, 5, 9))
    

