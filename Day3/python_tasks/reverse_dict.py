def reverse_dict(dict1):
    rev_dict={}
    for key in dict1:
        rev_dict[dict1[key]]=key
    return rev_dict
dict1={'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(dict1))