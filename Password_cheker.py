def check_password(password):
  length = len(password) >= 8
  upper = any(c.isuppe
