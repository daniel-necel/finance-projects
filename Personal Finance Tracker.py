import pandas as pd
import matplotlib.pyplot as plt

income = float(input("Enter your total monthly income (£): "))
tax_rate = float(input("Enter your tax rate (%): "))

net_income = income * (1 - tax_rate / 100)
print(f"Your income after {tax_rate}% tax is £{net_income:.2f}")

num_expenses = int(input("\nHow many expense categories do you have? "))

expenses = {}
for i in range(num_expenses):
    category = input(f"Enter category {i+1}: ")
    amount = float(input(f"Enter amount for {category} (£): "))
    expenses[category] = amount

total_expenses = sum(expenses.values())
savings = net_income - total_expenses

print("\n===== Budget Summary =====")
print(f"Total Income (after tax): £{net_income:.2f}")
print(f"Total Expenses: £{total_expenses:.2f}")

if savings > 0:
    print(f"Great job! You have £{savings:.2f} left over this month.")
elif savings == 0:
    print("You've perfectly balanced your budget this month.️")
else:
    print(f"it seems you have over budget by £{abs(savings):.2f}. ")

print("\nExpense Breakdown:")
for category, amount in expenses.items():
    percent = (amount / net_income) * 100
    print(f"{category}: £{amount:.2f} ({percent:.1f}%)")

save = input("\nWould you like to save this summary? (y/n): ")
if save.lower() == "y":
    with open("budget_summary.csv", "w") as file:
        file.write("Category,Amount(£)\n")
        for category, amount in expenses.items():
            file.write(f"{category},{amount}\n")
        file.write(f"\nTotal Income (after tax),{net_income}\n")
        file.write(f"Total Expenses,{total_expenses}\n")
        file.write(f"Savings,{savings}\n")
    print("Saved as budget_summary.csv")

df = pd.DataFrame(list(expenses.items()), columns=["Category", "Amount (£)"])

plt.figure(figsize=(6, 6))
plt.pie(df["Amount (£)"], labels=df["Category"], autopct="%1.1f%%", startangle=90)
plt.title("Expense Breakdown by Category")
plt.show()

summary = {
    "Income (after tax)": net_income,
    "Expenses": total_expenses,
    "Savings": savings
}

plt.figure(figsize=(6, 4))
plt.bar(summary.keys(), summary.values(), color=["green", "red", "blue"])
plt.title("Monthly Financial Overview")
plt.ylabel("Amount (£)")
plt.show()
