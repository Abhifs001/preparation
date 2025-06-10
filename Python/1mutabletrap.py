# mutable_default_arguments.py

"""
 Problem: Mutable Default Arguments in Python

In Python, default argument values are evaluated **once** at the time the function is defined,
not each time the function is called. This means that if you use a **mutable object** like a list, dict, or set
as a default argument, it will be shared across all function calls.

This can lead to unexpected behavior, especially in production code dealing with
caching, logging, or accumulating data.
"""

#  Problematic version
def append_item_bad(my_list=[]):  # Default value is a shared list!
    my_list.append("data")
    return my_list

print(" Buggy Output (shared list):")
print(append_item_bad())  # ['data']
print(append_item_bad())  # ['data', 'data'] ← shared state issue
print(append_item_bad())  # ['data', 'data', 'data']


"""
 Common but Incorrect Fix: Reinitializing the list inside the function
This avoids the shared state issue, but it also ignores any passed-in list,
which defeats the purpose of accepting an argument.
"""

# Misleading fix
def append_item_wrong(my_list=[]):
    my_list = []  # Always resets — so argument is ignored
    my_list.append("data")
    return my_list

print("\nMisleading Fix (resets list every time):")
print(append_item_wrong())       # ['data']
print(append_item_wrong(['x']))  # ['data'] ← 'x' was ignored!


"""
Correct and Pythonic Solution

Use `None` as the default, then check inside the function.
If the argument is None, initialize a new list.
This ensures that:
- The default is NOT shared across calls
- Passed-in lists are respected
"""

def append_item_safe(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append("data")
    return my_list

print("\n Correct Fix (isolated or custom list):")
print(append_item_safe())            # ['data']
print(append_item_safe())            # ['data']
print(append_item_safe(['custom']))  # ['custom', 'data']


"""
 Summary:
- Never use mutable objects like [] or {} as default arguments
-Don’t reset the argument inside — it ignores passed values
-Use `None` as default, then initialize inside the function
"""

