# Defining exchange rates
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.96,
    'GBP': 0.80,
    'INR': 87.43,
    'PKR': 277.57,
    'JPY': 152.84,
    'usd': 1.0,
    'eur': 0.96,
    'gbp': 0.80,
    'inr': 87.43,
    'pkr': 277.57,
    'jpy': 152.84,
}

def convert_currency(amount: float, from_currency: str, to_currency: str):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency")
        return None
    
    # Converting the amount to USD first
    amount_in_usd = amount / exchange_rates[from_currency]
    
    # Converting the USD amount to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

# Getting user input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP, INR, PKR, JPY): ")
to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP, INR, PKR, JPY): ")

# Converting the user input
converted_amount = convert_currency(amount, from_currency, to_currency)

# Printing the result
if converted_amount is None:
    print("Invalid currency")
else:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")