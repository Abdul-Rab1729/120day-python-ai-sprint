def dict_from_lists(keys,values):
    dict1={}
    for i in range(len(keys)):
        dict1[keys[i]]=values[i]
    return dict1
keys = ["name", "age", "country"]
values = ["Abd", "21", "India"]
print(dict_from_lists(keys,values))