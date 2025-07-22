def common_elements(nums1, nums2):
    res=[]
    for x in nums1:
        for y in nums2:
            if x==y and x not in res:
                res.append(x)
    return res
