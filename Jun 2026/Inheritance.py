class Category:
    def __init__(self, name):
        self.name = name

    def get_type(self):
        return "generic"

class IncomeCategory(Category):
    def get_type(self):
        return "income"
    def is_taxable(self):
        return True

class ExpenseCategory(Category):
    def get_type(self):
        return "expense"