# def fetch_price(symbol):
#     try:
#         # simulate API hit
#         if symbol == "XYZ":
#             raise ValueError("Symbol not found")
#         return 1000  # dummy price
#     except ValueError as e:
#         print(f"[ERROR] {symbol}: {e}")
#         return None

# print(fetch_price("XYZ"))   # ➝ [ERROR] XYZ: Symbol not found


try:
    price = 1000
except:
    print("Error occurred")
else:
    print("No errors occurred, price is:", price)
finally:
    print("Closing DB connection/logging/etc")
