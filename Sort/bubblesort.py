"""
冒泡排序设计思想

对数列下标最小的元素开始，逐个比较指针元素与位置元素的大小，逆序则交换，顺序则不变，重复遍历到最后一个元素，则数列有序
<不稳定排序>
"""
from Sort.utils import format_input


def bubble_sort(alist):
    """冒泡排序"""
    if len(alist) <= 1:
        return alist
    for left in range(len(alist) - 1):
        for right in range(left + 1, len(alist)):
            if alist[left] >= alist[right]:
                alist[left], alist[right] = alist[right], alist[left]
    return alist


if __name__ == '__main__':
    while True:
        input_str = input('please input a seq which use "," to split or you can input "q" to quit :\n')
        input_arr = format_input(input_str)
        if not input_arr:
            break
        print(bubble_sort(input_arr))
