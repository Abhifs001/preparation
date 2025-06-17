#closures are the functions that can be defined inside another function
#closures can access the variables of the outer function even after the outer function has finished executing
#3,4,5--------------num+5
#function pass value -----3,4,5---------return x+5
# what if we want to return x+10, x+12 ---------will u create so many functions ? no 
# that's why closures are useful in Python,  

#for example, we can create a function that returns another function that increments a number by a given value
# this is a closure because the inner function can access the variable `increment` from the outer function
def make_incrementer(increment):
    def incrementer(x):
        return x + increment
    return incrementer

# create an incrementer that adds 5
increment_by_5 = make_incrementer(5)
# use the incrementer
print(increment_by_5(10))  # ➝ 15
print(increment_by_5(20))  # ➝ 25
print(increment_by_5(30))  # ➝ 35
# create an incrementer that adds 10
increment_by_10 = make_incrementer(10)
# use the incrementer
print(increment_by_10(10))  # ➝ 20

#let us know how the memory is managed in this case
# In this case, the `incrementer` function retains a reference to the `increment` variable from its enclosing scope (`make_incrementer`).
# This is possible because of closures in Python, which allow the inner function to "remember" the environment in which it was created.
# When `make_incrementer` is called, it creates a new scope with its own `increment` variable.
# When `incrementer` is returned, it retains access to that scope, even after `make_incrementer` has finished executing.
# This means that each time you call `make_incrementer`, a new closure is created with its own `increment` value.
# This is efficient in terms of memory because the inner function does not create a new copy of the `increment` variable; it simply retains a reference to it.
# This allows for efficient memory usage while still providing the functionality of closures. 