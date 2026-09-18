#unit conveter currency
def currency_converter(amount, from_currency, to_currency):
    # Define exchange rates
    exchange_rates = {
        'USD': 1.0,  # Base currency
        'EUR': 0.87,
        'KES': 129.0,
        'GBP': 0.75,
        'JPY': 156.0,
        'CAD': 1.40,
        'AUD': 1.40,
        'INR': 95.0
    }

    # Check if the currencies are valid
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Invalid currency code")

    # Convert amount to USD first, then to the target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = f"{amount_in_usd * exchange_rates[to_currency]:,.2f}"

    return converted_amount

amount=float(input("Enter the amount to convert: "))#ask user for amount
from_currency=input("Enter the currency code to convert from (e.g., USD, EUR, KES, GBP, JPY, CAD, AUD, INR): ").upper()#ask user for from currency
to_currency=input("Enter the currency code to convert to (e.g., USD, EUR, KES, GBP, JPY, CAD, AUD, INR): ").upper()#ask user for to currency
converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")