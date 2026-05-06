def check_password(password):
  length = len(password) >= 8
  upper = any(c.isupper() for c in
password)
  lower = any(c.islower() for c in
password)
  digit = any(c.isdigit() for c in
password)
  special = any(c in "!@#$%^&*" for c in
password)
  score = sum([length, upper, lower, digit, sepecial])
  if score == 5:
      print("Strong Password 💪")
  elif score >= 3:
      print("Medium Password 👍")
  else:
      print("Week Password ❌")
password = input("Enter Password: ")
check_password(password)
    
    
    

              
