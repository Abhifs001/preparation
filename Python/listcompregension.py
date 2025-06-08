import numpy
from typing import List

def cal_sqr(numbers: int)->List[int]:
    ans = [] 

    for i in range(1, numbers+1):
        ans.append(i*i)
    
    return ans


# ans = cal_sqr(10)


def cal_sqr2(numbers: int)->List[int]:
    ans = [ i*i for i in range(1,numbers)]
    
    return ans

ans = cal_sqr2(10)
print(ans)
