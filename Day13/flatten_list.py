def flatten_list(list1):
    result = []
    stack = [list1]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result

list1=[[1,2],[3,[4,5]]]
print(flatten_list(list1))