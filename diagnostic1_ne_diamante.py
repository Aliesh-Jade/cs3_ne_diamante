
def calculate_checkout(cart_total, shipping_speed):
   if shipping_speed == "Express":
      shipping_cost = 20
   elif shipping_speed == "Overnight":
      shipping_cost = 35
   elif shipping_speed == "Standard":
      shipping_cost = 10
   elif cart_total >= 100:
      shipping_cost = 0
   else:
      print("Error")
      shipping_cost = 0

   return f"Your total is: ${cart_total + shipping_cost}"

print(calculate_checkout(10000, "Express"))
