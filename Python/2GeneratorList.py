# generators_basics.py

# -------------------------------------------
# 📌 Section 1: Generator Expression vs List
# -------------------------------------------

# List comprehension (eager evaluation)
squares_list = [x**2 for x in range(10)]
print("List of squares:", squares_list)

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(10))
print("First 3 squares using generator:")
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4


# -------------------------------------------
# 📌 Section 2: Generator Function with `yield`
# -------------------------------------------

def number_stream(n):
    """Yields squares from 0 to n-1"""
    for i in range(n):
        yield i * i

print("\nSquares from number_stream:")
for val in number_stream(5):
    print(val)


# -------------------------------------------
# 📌 Section 3: Streaming Large File (Simulated)
# -------------------------------------------

def read_large_file(filename):
    """Simulates line-by-line file reading using a generator."""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()  # Remove newline

# Uncomment this to test with a large file
# for line in read_large_file('big_file.txt'):
#     process(line)


# -------------------------------------------
# 📌 Section 4: Infinite Generator (Use With Care)
# -------------------------------------------

def infinite_counter(start=0):
    """Yields an infinite stream of incrementing numbers."""
    while True:
        yield start
        start += 1

print("\nFirst 5 numbers from infinite_counter:")
counter = infinite_counter()
for _ in range(5):
    print(next(counter))


# -------------------------------------------
# 📌 Section 5: Chaining Generators (Pipeline)
# -------------------------------------------

def generate_numbers():
    for i in range(1, 6):
        yield i

def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

print("\nChained Generator Pipeline Output (even squares):")
nums = generate_numbers()
squares = square_numbers(nums)
even_squares = filter_even(squares)

for val in even_squares:
    print(val)


#Section 6: Infinite generators 
def stream_forever():
    i = 0
    while True:
        yield i
        i += 1

gen = stream_forever()
next(gen)  # 0
next(gen)  # 1

