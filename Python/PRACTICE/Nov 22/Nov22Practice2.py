def main():
        
        #initialize variable
        original_amount = 0
        
        while original_amount == 0:
            original_amount_string = (input("Please enter the original amount $"))

            try:
                  original_amount = float(original_amount_string)
                  
            except ValueError:
                  print("Hey is it too hard to enter a number?!?!")

                     
                

        price_with_tax = original_amount * 1.15

        print(f"Price with taxt is ${price_with_tax:.2f}")

if __name__ == "__main__":
      main()
