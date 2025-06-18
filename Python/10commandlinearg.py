# #args and kwargs are used to pass a variable number of arguments to a function.
# ## args is used to pass a variable number of non-keyword arguments,
# ## while kwargs is used to pass a variable number of keyword arguments.
# def log_trade(*args, **kwargs):
#     print("ARGS:", args)
#     print("KWARGS:", kwargs)

# log_trade("TCS", 4500, 100, order_type="BUY", exchange="NSE")

def batch_order(*orders):
    for order in orders:
        print(f"Placing order for {order['symbol']} at {order['price']}")

batch_order(
    {"symbol": "TCS", "price": 3200},
    {"symbol": "WIPRO", "price": 520},
    {"symbol": "HDFC", "price": 1800}
)

# This function takes a variable number of orders and prints the details of each order.

# Feature	Use Case
# *args	Accept unlimited positional arguments
# **kwargs	Accept unlimited keyword arguments
# * unpacking	Pass values from list/tuple into a function
# ** unpacking	Pass values from dict into a function
# Useful For	Logging, wrappers, APIs, dynamic configs