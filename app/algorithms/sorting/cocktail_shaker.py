def cocktail_shaker_sort(nums:list)->list:
    l = len(nums)
    for i in range(l//2):
        for j in range(i,l-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
        for j in range(l-i-2,i-1):
            if nums[j]< nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
        
    return nums