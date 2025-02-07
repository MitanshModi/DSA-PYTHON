import heapq

class Expense:
    def __init__(self, description, amount, priority):
        self.description = description
        self.amount = amount
        self.priority = priority

    def __lt__(self, other):
        # This makes the heap act like a max-heap by comparing priorities.
        return self.priority > other.priority

    def __repr__(self):
        return f"Expense(description={self.description}, amount={self.amount}, priority={self.priority})"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, priority):
        # Create a new expense object and add it to the heap
        expense = Expense(description, amount, priority)
        heapq.heappush(self.expenses, expense)

    def remove_highest_priority_expense(self):
        # Remove the expense with the highest priority (i.e., max priority)
        if self.expenses:
            return heapq.heappop(self.expenses)
        else:
            return None

    def view_expenses(self):
        # View all expenses in the priority queue
        return sorted(self.expenses, key=lambda x: x.priority, reverse=True)

    def total_expenses(self):
        # Calculate the total amount of expenses
        return sum(expense.amount for expense in self.expenses)


# Example usage of the Expense Tracker
def main():
    tracker = ExpenseTracker()

    # Adding some expenses
    tracker.add_expense("Groceries", 50, priority=3)
    tracker.add_expense("Rent", 1200, priority=1)
    tracker.add_expense("Utilities", 100, priority=2)
    tracker.add_expense("Dining Out", 30, priority=4)

    # View all expenses (sorted by priority)
    print("All Expenses (Sorted by Priority):")
    for expense in tracker.view_expenses():
        print(expense)

    # Remove the highest priority expense
    print("\nRemoving highest priority expense:")
    highest_priority_expense = tracker.remove_highest_priority_expense()
    print(highest_priority_expense)

    # View remaining expenses
    print("\nRemaining Expenses:")
    for expense in tracker.view_expenses():
        print(expense)

    # View total expenses
    print(f"\nTotal Expenses: ${tracker.total_expenses()}")

if __name__ == "__main__":
    main()
