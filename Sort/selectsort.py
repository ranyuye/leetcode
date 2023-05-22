"""
选择排序
选择排序和冒泡排序非常相似，区别在于 选择排序每次遍历仅交换一次，冒泡排序则需要交换多次
<不稳定排序> [时间复杂度 O(n ^ 2)] {空间复杂度O(1)}

"""
from Sort.utils import format_input


def select_sort(alist) -> list:
    if len(alist) <= 1:
        return alist
    for left in range(len(alist) - 1):
        flag = left
        for right in range(left + 1, len(alist)):
            if alist[right] < alist[flag]:
                flag = right
        alist[flag], alist[left] = alist[left], alist[flag]
    return alist


if __name__ == '__main__':
    while True:
        input_str = input('please input a seq which use "," to split or you can input "q" to quit :\n')
        input_arr = format_input(input_str)
        if not input_arr:
            break
        print(select_sort(input_arr))
