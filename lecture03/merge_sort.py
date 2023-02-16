from random import randint


def merge_sort(nums, log=False):
    if len(nums) > 1:
        mid_index = len(nums) // 2
        left = nums[:mid_index]
        right = nums[mid_index:]
        print(left, '|', right)
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                print('l|', end='')
            else:
                nums[k] = right[j]
                j += 1
                print('r|', end='')
            print(nums[k], end='|<|')
            k += 1

        while i < len(left):
            nums[k] = left[i]
            print(nums[k], end='|l|')
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            print(nums[k], end='|r|')
            j += 1
            k += 1
        print()


size = int(input('Введите размер списка: '))

list1 = [randint(0, 100) for i in range(size)]
print(list1)
merge_sort(list1, log=True)
print(list1)
