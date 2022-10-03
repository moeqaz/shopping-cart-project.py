from IPython.display import clear_output

def items_to_purchase():
    
    shopping_cart = []
    
    while True:
        
        items = input('What would you like to add to your shopping cart? ')
        price = input(f'What is the price of the {items}?: ')
        quantity = input(f'How many {items}s would like to add?: ')
        total_price = {price}

        print(f"{quantity} {items}s have been added to your cart for {price} each.")
        print(f"Your current cart: {quantity} {items}s x ${price}")
        
        ask = input("Would you like to Add/Remove/Show/Quit? ")
        if ask not in {'add', 'remove', 'show', 'quit'}:
            ask = input("Not a valid response! Please respond with 'Continue', 'Remove', 'Checkout', or 'Quit' ")    
        
        elif ask == 'remove':
            for items, price in shopping_cart():
                print(f"This is your shopping cart so far.")
                print({shopping_cart})
                ask = input('What item would you like to remove?')
 
        elif ask == 'show':
            for items, price in shopping_cart.items():
                print(f"This is your shopping cart so far.")
                shopping_cart[items] = (price, quantity)
                print(shopping_cart)
                total_price = {price}

            total_price += f'Total: ${total_price:.2f}'
            print(total_price)
            
        else:
            pass

                
        for items, (price, quantity) in shopping_cart.items():
                    print(f"Thank you for shopping with us! Your receipt is shown below.")

        shopping_cart[items] = (price, quantity)    

print(items_to_purchase())        