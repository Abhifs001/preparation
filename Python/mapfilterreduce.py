numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mappedNumbers = list(map(lambda x: x * x, numbers)) 

# print(mappedNumbers)  

# filtereredNumbers = list(filter(lambda x: x%2==0 , numbers))
# print(filtereredNumbers)

# from functools import reduce
# reducedNumbers = reduce(lambda x,y: x+y, numbers)
# print(reducedNumbers)

raw_data = ['  TCS.IN ', ' INFY.NS ', ' RELIANCE.BSE ']
cleaned_data = list(map(lambda x: x.strip().upper(), raw_data))

print(cleaned_data)