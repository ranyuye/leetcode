"""
快排的设计思想

从 待排序 数列中挑出一个基准数，一般是数列中第一个数字；后有两个指针分别从头和尾进行遍历查找，找第一个小于基准数的值，将他们交换；
之后从基准数的下一个位置再进行查找，直到头尾指针相遇结束
<递归的>

"""

def quick_sort(arr, start, end):
    """快速排序"""
    if start >= end:
        return

    mid = arr[start]  # set mid-number
    left, right = start, end  # left and right imply where are we starting place and ending place with arr;
    while left < right:
        while left < right and arr[right] >= mid:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < mid:
            left += 1
        arr[right] = arr[left]
    arr[left] = mid  # amend mid-number place
    quick_sort(arr, start, right - 1)  # quick_sort with left seq
    quick_sort(arr, left + 1, end)  # quick_sort with right seq


if __name__ == '__main__':
    while True:
        input_str = input('please input a seq which use "," to split or you can input "q" to quit :\n')
        if input_str == 'q':
            break
        input_arr = input_str.split(',')
        input_arr = list(map(lambda x: int(x), input_arr))
        quick_sort(input_arr, 0, len(input_arr) - 1)
        print(input_arr)
