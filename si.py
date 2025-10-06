
principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (R) in %: "))
time = float(input("Enter the time in years (T): "))
simple_interest = (principal * rate * time) / 100
compound_interest = principal * ((1 + rate / 100) ** time) - principal
print("\n--- Interest Report ---")
print(f"Principal Amount: ₹{principal:.2f}")
print(f"Rate of Interest: {rate:.2f}%")
print(f"Time Period: {time:.2f} years")
print(f"Simple Interest: ₹{simple_interest:.2f}")
print(f"Compound Interest: ₹{compound_interest:.2f}")
