#摘抄自《玩转Python轻松过二级》
#二分查找
def binarySearch(lst,value):
    start = 0
    end =len(lst)
    while start <end:
        middle = (start + end) //2
        if value == lst[middle]:
            return middle
        elif value >lst[middle]:
            start = middle + 1
        elif value <lst[middle]:
            start = middle - 1
    return False
from random import randint

lst = [randint(1,50) for i in range(20)]
lst.sort()
print(lst)
result = binarySearch(lst,30)
if result != False:
    print("Success,its position is ：",result)
else:
    print("Fail.Not exist")

    
