"""
CP1404 2022 Prac 01
Erica Finlay

Practice & Extension Work
2. Electricity Bill Estimator

Pseudocode:
display title
get price (kWh)
get daily_use (kWh)
get length_of_billing_period (days)
total_bill = price * daily_use * length_of_billing_period
display total_bill
"""

print("Electricity bill estimator")
price = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
length_of_billing_period = int(input("Enter number of billing days: "))
total_bill = (price / 100) * daily_use * length_of_billing_period
print(f"Estimated bill: ${total_bill:.2f}")

"""
Pseudocode:
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

display title
get tariff
while user_tariff_choice != 11 and user_tariff_choice != 13
    display error message
    get tariff
if user_tariff_choice = 11
     tariff = TARIFF_11
else
    tariff = TARIFF_31
get daily_use (kWh)
get length_of_billing_period (days)
total_bill = tariff * daily_use * length_of_billing_period
display total_bill
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
user_tariff_choice = int(input("Which tariff? 11 or 31: "))
while user_tariff_choice != 11 and user_tariff_choice != 13:
    print("Invalid response.  Please enter either 11 or 31.")
    user_tariff_choice = float(input("Which tariff? 11 or 31: "))
if user_tariff_choice == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
daily_use = float(input("Enter daily use in kWh: "))
length_of_billing_period = int(input("Enter number of billing days: "))
total_bill = tariff * daily_use * length_of_billing_period
print(f"Estimated bill: ${total_bill:.2f}")
