principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the rate of interest per annum (R): "))
time = float(input("Enter the time in years (T): "))


simple_interest = (principal * rate * time) / 100

print(f"\nSimple Interest = ₹{simple_interest:.2f}")
