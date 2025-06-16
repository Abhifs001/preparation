# Normal function
def square(x):
    return x * x

# Lambda version
square_lambda = lambda x: x * x

print(square(4))         # ➝ 16
print(square_lambda(4))  # ➝ 16

# A lambda is an anonymous (nameless) function defined in a single line.

# Used when the function is simple and won’t be reused elsewhere.

