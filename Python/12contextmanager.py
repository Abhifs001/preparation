# f = open("trades.txt")
# data = f.read()
# f.close()
# If something fails before .close(), the file remains open – 🔥 not acceptable in production!


# with open("trades.txt", 'r') as f:
#     data = f.read()
# # The file is automatically closed when the block is exited, even if an error occurs

# def read_orders(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             return f.readlines()
#     except FileNotFoundError:
#         print("Order file not found!")
#         return []

# import sqlite3

# with sqlite3.connect("market.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM trades")


# class DummyConnection:
#     def __enter__(self):
#         print("Starting connection")
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Closing connection")

# with DummyConnection():
#     print("Processing trade data...")


from contextlib import contextmanager

@contextmanager
def connect():
    print("Start")
    yield
    print("Close")

with connect():
    print("Work with finance data")

################################################################################################
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        # Return False to propagate exceptions (if any)
        return False

#using FileManager
with FileManager("trades.txt", "r") as f:
    data = f.read()
    print(data)
 

 