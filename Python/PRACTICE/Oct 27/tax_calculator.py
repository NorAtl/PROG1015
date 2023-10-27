myVariable = "A" #Global

def calculateTax(in_product_price, in_tax_rate):
    product_total = in_product_price * ( 1 + in_tax_rate)#Local
    return product_total

def main():
    product_one_price = float(input("\nEnter Product one price: $"))#Local
    product_one_total = calculateTax(product_one_price, 0.15)#Local
    print((f"The total price is ${product_one_total:.2f}\n"))

    product_two_price = float(input("\nEnter Product two price: $"))#Local
    product_two_total = calculateTax(product_two_price, 0.15)#Local
    print((f"The total price is ${product_two_total:.2f}\n"))
    print(myVariable)

if __name__ == "__main__":
    main()