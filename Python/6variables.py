
# Python uses the LEGB rule for name resolution:

# Local

# Enclosing

# Global

# Built-in

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()  # ➝ local
# In this example, the `inner` function has its own local variable `x`,
