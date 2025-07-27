def merge_two_dict():
    freq1={"a": 2,"b":1,"c":2}
    freq2={"c":1, "d":3, "g":1}

    for x in freq2:
        if x not in freq1:
            freq1[x]=freq2[x]
        else:
            freq1[x]+=freq2[x]
    return freq1

print(merge_two_dict())