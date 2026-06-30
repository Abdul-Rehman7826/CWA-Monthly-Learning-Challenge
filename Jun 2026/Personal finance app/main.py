import os
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

# ------------------- 1. MODEL (OOP) -------------------
class Transaction:
    def __init__(self, amount, category, trans_type, date=None):
        self.amount = amount
        self.category = category
        self.type = trans_type  # "income" or "expense"
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        
        # Validation using encapsulation logic
        if self.amount <= 0:
            raise ValueError("Amount must be positive.")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        # Remove the MongoDB '_id' field if it exists to avoid errors
        return Transaction(
            amount=data["amount"],
            category=data["category"],
            trans_type=data["type"],
            date=data["date"]
        )

# ------------------- 2. REPOSITORY (NoSQL CRUD) -------------------
class TransactionRepository:
    def __init__(self, collection):
        self.collection = collection

    def save(self, transaction):
        return self.collection.insert_one(transaction.to_dict()).inserted_id

    def get_all(self):
        docs = self.collection.find({})
        return [Transaction.from_dict(doc) for doc in docs]

    def delete(self, doc_id):
        return self.collection.delete_one({"_id": ObjectId(doc_id)})

    def get_summary_stats(self):
        # Using MongoDB Aggregation for efficiency
        pipeline = [
            {"$group": {
                "_id": "$type",
                "total": {"$sum": "$amount"}
            }}
        ]
        results = self.collection.aggregate(pipeline)
        stats = {"income": 0.0, "expense": 0.0}
        for item in results:
            stats[item["_id"]] = item["total"]
        return stats

    def get_category_spending(self):
        pipeline = [
            {"$match": {"type": "expense"}},
            {"$group": {
                "_id": "$category",
                "total": {"$sum": "$amount"}
            }},
            {"$sort": {"total": -1}}
        ]
        return list(self.collection.aggregate(pipeline))

# ------------------- 3. CONTROLLER / CLI (The App) -------------------
class FinanceApp:
    def __init__(self, repo):
        self.repo = repo

    def run(self):
        while True:
            print("\n" + "="*30)
            print("💰 PERSONAL FINANCE TRACKER")
            print("="*30)
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View All")
            print("4. Summary")
            print("5. Category Report")
            print("6. Delete")
            print("7. Exit")
            
            choice = input("👉 Select option: ")

            if choice == "1": self._add("income")
            elif choice == "2": self._add("expense")
            elif choice == "3": self._view_all()
            elif choice == "4": self._summary()
            elif choice == "5": self._category_report()
            elif choice == "6": self._delete()
            elif choice == "7": 
                print("👋 Exiting. Have a great day!")
                break
            else:
                print("❌ Invalid choice.")

    def _add(self, t_type):
        try:
            amt = float(input("Amount: "))
            cat = input("Category: ")
            date = input("Date (YYYY-MM-DD, skip for today): ") or None
            t = Transaction(amt, cat, t_type, date)
            self.repo.save(t)
            print("✅ Added successfully.")
        except ValueError as e:
            print(f"❌ Error: {e}")

    def _view_all(self):
        items = self.repo.get_all()
        if not items:
            print("📭 No transactions.")
            return
        for idx, t in enumerate(items, 1):
            print(f"{idx}. {t.date} | {t.category} | ${t.amount:.2f} | {t.type}")

    def _summary(self):
        stats = self.repo.get_summary_stats()
        income = stats.get("income", 0.0)
        expense = stats.get("expense", 0.0)
        print(f"📈 Income:  ${income:.2f}")
        print(f"📉 Expense: ${expense:.2f}")
        print(f"⚖️ Balance: ${income - expense:.2f}")

    def _category_report(self):
        data = self.repo.get_category_spending()
        if not data:
            print("No expenses recorded.")
            return
        print("📊 Top Spending Categories:")
        for item in data:
            print(f"  - {item['_id']}: ${item['total']:.2f}")

    def _delete(self):
        self._view_all()
        # We don't easily have IDs in the view. For simplicity, we ask user to input ID.
        # In a real app, we'd display IDs too. Let's just use the ID from DB.
        all_docs = list(self.repo.collection.find({}))
        if not all_docs:
            return
        print("\nAvailable IDs:")
        for doc in all_docs:
            print(f"ID: {doc['_id']} | {doc['date']} | {doc['category']} | ${doc['amount']}")
        doc_id = input("Enter the exact ID string to delete: ")
        try:
            result = self.repo.delete(doc_id)
            if result.deleted_count > 0:
                print("🗑️ Deleted.")
            else:
                print("❌ ID not found.")
        except:
            print("❌ Invalid ID format.")

# ------------------- 4. MAIN EXECUTION -------------------
if __name__ == "__main__":
    # Connect to MongoDB (Default localhost)
    try:
        client = MongoClient("mongodb+srv://admin:admin@cluster0.lno9k6g.mongodb.net/?appName=Cluster0&compressors=zlib")
        db = client["finance_tracker_db"]
        collection = db["transactions"]
        print("✅ Connected to MongoDB successfully.")
    except Exception as e:
        print(f"❌ Could not connect to MongoDB. Error: {e}")
        print("Make sure MongoDB is running (mongod). Exiting.")
        exit(1)

    repo = TransactionRepository(collection)
    app = FinanceApp(repo)
    app.run()