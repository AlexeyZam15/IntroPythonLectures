def merge_sort(nums):
    if len(nums) > 1:
        mid_index = len(nums) // 2
        left = nums[:mid_index]
        right = nums[mid_index:]
        print(left,'|',right)
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                print('l|',end='')
            else:
                nums[k] = right[j]
                j += 1
                print('r|',end='')
            print(nums[k],end='|<|')
            k += 1
            
        while i < len(left):
            nums[k] = left[i]
            print(nums[k],end='|l|')
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            print(nums[k],end='|r|')
            j += 1
            k += 1
        print()
            
list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)