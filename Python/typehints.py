name: str= "Data Engineer"
count: int = 10 

ratio: float= 0.04


from typing import List

def filter_number(numbers: List[int], limit: int= 100)->List[int]:
  """  this is docstring for documentation purpose """
  ans = [i for i in numbers if i> limit]

  return ans 


arr= [ i for i in range(1000)]

ans = filter_number(arr)

print(ans)

