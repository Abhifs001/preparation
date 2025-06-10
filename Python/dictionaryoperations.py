#dictionary comprehensions are much faster in real world scenario 

prices = { 'banana': 0.99, 'apple': 1.49, 'orange': 0.79 }

discount_prices = {fruit: prevPrice*0.9 for fruit, prevPrice in prices.items()}

print(discount_prices)

