balance = 10000
pin = 1234
print("--- welcome to ATM ---")
input_pin = int(input("Enter PIN: "))
if input_pin == pin:
  print("1. Check Balance")
  print("2. withdraw Money")
  choice = int(input("Choose an option (1 or 2): "))
  if choice == 1:
    print(f"Your Balance is: {balance}")
  elif choice == 2:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
      balance -= amount 
      print(f"Withdraw Successful! Remaining Balance: {balance}")
   else:
     print("Insufficient Funds!")
else:
  print("worng PIN! Try again.")

    
    
             
