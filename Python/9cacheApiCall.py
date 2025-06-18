import logging
import time 
loging = logging.basicConfig(level=logging.INFO)

def loggin_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"calling function {func.__name__} with args : {args} and kwargs : {kwargs} ".format(args, kwargs))
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"function {func.__name__} took {end - start} seconds to execute")
        return result
    return wrapper                
                
                
def stock_price_cache():
    cache = {}
    @loggin_decorator
    def get_price(symbol):
        if symbol in cache:
            print("Fetching from cache...")
            return cache[symbol]
        print("Fetching from API...")
        # Simulate expensive call
        price = len(symbol) * 100  # dummy price
        cache[symbol] = price
        return price

    return get_price

get_price = stock_price_cache()
print(get_price("TCS"))   # API
print(get_price("TCS"))   # Cache 

