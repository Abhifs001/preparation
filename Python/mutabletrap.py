# problem 
# In Python, using mutable default arguments like [], {}, or set() can lead to unexpected behavior because the same object is reused across function calls. This causes shared state and bugs that are hard to trace. To avoid this, always use None as the default and initialize the mutable object inside the function. This ensures each call gets a fresh object unless one is explicitly passed.

def append_item(my_list=None):
    my_list = []
    my_list.append("data")
    return my_list

print(append_item())  # ['data']
print(append_item())  # ['data', 'data'] ← Bug?

# Here's the correct and Pythonic way to handle it: repsect arg and create new if arg is none 
def append_item(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append("data")
    return my_list


# def append_item(my_list=[]): # do not use mutable default arguements
#     my_list.append("data")
#     return my_list

# print(append_item(['00']))
# print(append_item())