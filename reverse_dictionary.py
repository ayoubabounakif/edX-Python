############################## REVIEW ###############################

def reverse_dictionary(dict):
    invert = {}
    for key in dict:
        for value in dict[key]:
            key_lowered = key.lower()
            value_lowered = value.lower()
            if invert.get(value_lowered):
                if key not in invert[value_lowered]:
                    invert[value_lowered].append(key_lowered)
                    invert[value_lowered].sort()
            else:
                invert[value_lowered] = [key_lowered]
    return invert

def invert_dict(d):
    return dict((v, k) for k in d for v in d[k])

def invert_dol_nonunique(d):
    newdict = {}
    for k in d:
        for v in d[k]:
            k = k.lower()
            v = v.lower()
            newdict.setdefault(v, []).append(k)
            newdict.setdefault(v, []).sort()
    return newdict

d = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], \
'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}
print (invert_dict(d))

print (reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], \
'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))

print (invert_dol_nonunique({'Accurate': ['exact', 'precise'], 'exact': ['precise'], \
'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))
