def calculate_discount(price, discount_percent):
    #to confirm if the discount percentage is greater than 20%
   if discount_percent >= 20:
      #to calculate the net discount
      net_disount = price * (discount_percent/100)
      #to calculate the final price after applying the discount

      finalPrice = price - net_disount
      return finalPrice
   else:
      return price
   
   #to prompt the user for input

   price = input("Please Enter the Initial Price of the item : ")
   discount_percent = input ("Please enter the discount percentage: ")

   if finalPrice != price:
      print(f"The final price is: ${final_price}")
   else :
      print(f"The original price is : ${price}")
      
    