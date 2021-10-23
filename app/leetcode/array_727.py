# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
from typing import List


def remov_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        print('0, nums = []')
        return 0

    cursor = {'value': nums[0], 'index': 0}
    for i in range(1, len(nums)):
        if cursor['value'] == nums[i]:
            nums[i] = None
        else:
            cursor = {'value': nums[i], 'index': i}

    cursor = 0
    for i in range(1, len(nums) - 1):
        if nums[i] is None:
            if cursor < i:
                cursor = i
            for j in range(cursor + 1, len(nums)):
                if nums[j] is not None:
                    nums[i] = nums[j]
                    nums[j] = None
                    cursor = j
                    break
    cursor = 0
    for i in range(len(nums)):
        if nums[i] is not None:
            cursor = i
        else:
            break

    b = (''.join(str(nums).split())).replace('None', '_')
    print(f'{cursor + 1}, nums = {b}')

    return cursor + 1

remov_duplicates([1, 2])
remov_duplicates([])
remov_duplicates([1])
remov_duplicates([1, 1])
remov_duplicates([1, 1, 1])
remov_duplicates([1, 2, 2, 2])
remov_duplicates([1, 1, 2])
remov_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

from test_727 import big
remov_duplicates(big)

# python.exe .\app\leetcode\array_727.py