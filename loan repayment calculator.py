

import pandas as pd
import matplotlib.pyplot as plt

def calculate_loan(amount, interest_rate, years):
    monthly_rate = interest_rate / 100 / 12
    total_months = years * 12

    monthly_payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -total_months)

    total_paid = monthly_payment * total_months
    total_interest = total_paid - amount

    return monthly_payment, total_paid, total_interest, total_months

print("Welcome to the Loan Repayment Calculator!")

loan_amount = float(input("Enter how much you want to borrow (£): "))
rate = float(input("Enter the annual interest rate (%): "))
term_years = int(input("Enter how many years to repay: "))

monthly_payment, total_paid, total_interest, total_months = calculate_loan(loan_amount, rate, term_years)

print("\n===== Loan Summary =====")
print(f"Loan amount: £{loan_amount:,.2f}")
print(f"Interest rate: {rate:.2f}%")
print(f"Loan term: {term_years} years ({total_months} months)")
print(f"Monthly payment: £{monthly_payment:,.2f}")
print(f"Total repaid: £{total_paid:,.2f}")
print(f"Total interest paid: £{total_interest:,.2f}")

schedule = []
remaining_balance = loan_amount

for month in range(1, total_months + 1):
    interest = remaining_balance * (rate / 100 / 12)
    principal = monthly_payment - interest
    remaining_balance -= principal
    if remaining_balance < 0:
        remaining_balance = 0
    schedule.append([month, interest, principal, remaining_balance])

repayments = pd.DataFrame(schedule, columns=["Month", "Interest (£)", "Principal (£)", "Balance (£)"])

print("\n===== First 12 Months =====")
print(repayments.head(12).to_string(index=False))

plt.figure(figsize=(8, 5))
plt.plot(repayments["Month"], repayments["Interest (£)"], label="Interest", color="red")
plt.plot(repayments["Month"], repayments["Principal (£)"], label="Principal", color="green")
plt.title("Loan Repayment Breakdown Over Time")
plt.xlabel("Month")
plt.ylabel("Amount (£)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

save = input("\nWould you like to save this schedule as a CSV file? (y/n): ")
if save.lower() == "y":
    repayments.to_csv("loan_schedule.csv", index=False)
    print("Saved as 'loan_schedule.csv'")
