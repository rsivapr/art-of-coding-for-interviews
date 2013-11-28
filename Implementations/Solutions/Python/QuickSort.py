from random import randint

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot_ix = randint(0, len(lst)-1)
        pivot = lst[pivot_ix]
        lesser, greater = [], []
        for index in range(len(lst)):
            if  index == pivot_ix:
                pass
            else:
                ele = lst[index]
                if ele < pivot:
                    lesser.append(ele)
                else: 
                    greater.append(ele)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

