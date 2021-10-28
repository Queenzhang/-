# 分而治之

# 求数组元素的和
def sum(list):
    if list == []:
        return 0
    return list[0]+sum(list[1:])

# 计算列表包含的元素数
def count(list):
    if list == []:
        return 0
    return 1+count(list[1:])

# 找出列表中最大的数字
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max



# 快速排序
# 性能高度依赖于选择的基准值，所以每次随机地选择一个数组元素作为基准值
# 并行版本所需的时间为 O(n)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10,5,2,3]))