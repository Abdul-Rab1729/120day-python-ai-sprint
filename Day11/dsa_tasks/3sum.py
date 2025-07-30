def three_sum(list1):
    list1.sort()
    n = len(list1)
    res = []

    for i in range(n - 2):
        if i > 0 and list1[i] == list1[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = list1[i] + list1[left] + list1[right]
            if total == 0:
                res.append((list1[i], list1[left], list1[right]))
                left += 1
                right -= 1

                while left < right and list1[left] == list1[left - 1]:
                    left += 1
                while left < right and list1[right] == list1[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return res


list1 = [-1, 0, 1, 2, -1, -4]
print(three_sum(list1))
