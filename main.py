# -*- coding: utf-8 -*-
def merge(*arrs):
    arr_sum = [] 
    for i in arrs:
        arr_sum += i

    if len(arr_sum) < 2:
        return arr_sum

    else:
        const = arr_sum[0] 
        less = [i for i in arr_sum[1:] if i <= const] 
        greater = [i for i in arr_sum[1:] if i > const]
        
    return merge(less) + [const] + merge(greater)