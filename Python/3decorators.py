import time
import logging 


logging.basicConfig(level=logging.INFO 
                   , format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__)
def logging(func):
    def wrapper(*args, **kargs):
       
        start = time.time()
        logger.info(f"calling {func.__name__} with args: {args} and kwargs: {kargs}")
        result = func(*args, **kargs)
        end = time.time() 
        logger.info(f"{func.__name__} took {end - start:.4f} seconds")
        print(f"{func.__name__} return  {result}")
        return result
    return wrapper 



@logging
def printfunc(str):
    print( "hi ", str, " 2x2 is 4")
    return 


printfunc("abhinav")

