# import tax_calculator
from tax_calculator import calculateTax
# from tax_calculator import *

def main():
    product_price = float(input("\nEnter coffee price: $"))
    # product_total = tax_calculator.calculateTax(product_price, 0.15)
    product_total = calculateTax(product_price, 0.15)
    print((f"The total price is ${product_total:.2f}\n"))

if __name__ == "__main__":
    main()