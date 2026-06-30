

from pymongo import MongoClient

# Replace the placeholders with your actual credentials
connection_string = "mongodb+srv://admin:admin@cluster0.lno9k6g.mongodb.net/?appName=Cluster0&compressors=zlib"
client = MongoClient(connection_string)

# Connect to your database
db = client["finance_tracker_db"]

# Access your collection
collection = db["transactions"]

print("Successfully connected to MongoDB Atlas!")

class Transaction:
    transaction_count = 0

    # Instance constructor
    def __init__(self, amount, category, trans_type, date):
        self.amount = amount
        self.category = category
        self.type = trans_type 
        self.date = date
        Transaction.transaction_count += 1

   
    def display(self):
        return f"{self.date} | {self.category}: ${self.amount:.2f} ({self.type})"

t = Transaction(50.0, "Freelance", "income", "2026-06-09")
print(t.display())
