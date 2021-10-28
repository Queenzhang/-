#二分查找
#输入--->有序的元素列表
#输出--->元素出现的位置
#运行时间--->log n
#大O表示法--->O(log n)

def binery_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high
        mid = (low+high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


# 二分查找是一种分而治之的算法
# 基线条件 数组只包含一个元素，查找的值与目标值相同，就找到了！否则，说明他不在数组中
# 递归条件 将数组分成两半