def calculate_returning_amount(amount_due, amount_paid):
    if amount_paid < amount_due:
        return f"Insufficient payment. You still owe {amount_due - amount_paid:.2f}."
    else:
        return f"Returning amount: {amount_paid - amount_due:.2f}."

amount_due = float(input("Enter the amount due: "))
amount_paid = float(input("Enter the amount paid: "))

result = calculate_returning_amount(amount_due, amount_paid)
print(result)
