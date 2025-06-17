#suppose you want to count the number of times a API is hit 
# general approach is create a global variable count and increment it every time the API is hit


# count = 0  
# def api_hit():
#     global count
#     count += 1
#     return f"API has been hit {count} times."

# This approach works, but it has a drawback: the `count` variable is global, which means it can be modified from anywhere in the code.


# A better approach is to use a closure to encapsulate the `count` variable, making it private to the `api_hit` function.

def make_api_hit_counter():
    count = 0  # This count is now private to the closure

    def api_hit():
        nonlocal count  # Use nonlocal to modify the outer variable
        count += 1
        return f"API has been hit {count} times."

    return api_hit

counter = make_api_hit_counter()
print(counter())  # ➝ "API has been hit 1 times."
print(counter())  # ➝ "API has been hit 2 times."
print(counter())  # ➝ "API has been hit 3 times."

