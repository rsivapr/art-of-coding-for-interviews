"""
Things to do:
* Watch out for repeating elements.

"""

def merge(sl1, sl2):
    new_list = []
    while len(sl1) > 0 or len(sl2) > 0:
        #print len(sl1), len(sl2)
        if len(sl1) > 0 and len(sl2) > 0:
            if sl1[:1] < sl2[:1]:
                new_list += sl1[:1]
                sl1 = sl1[1:]
            elif sl1[:1] > sl2[:1]:
                new_list += sl2[:1]
                sl2 = sl2[1:]
        elif len(sl1)>0:
            new_list += sl1
            sl1 = []
        else:
            new_list += sl2
            sl2 = []
    return new_list

def merge_sort(lst):
    """
    Worst case performance:         O(n*log(n))
    Best case performance:          O(n*log(n))
    Average case performance:       O(n*log(n))
    Worst case space complexity:    O(n)
    """
    if len(lst) <= 1:
        return lst
    else:
        left = merge_sort(lst[:len(lst)/2]) 
        right = merge_sort(lst[len(lst)/2:])
        return merge(left, right)


