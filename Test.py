user_input = input("Enter Expression:")
result = eval(user_input) # Unsafe

import hashlib

def insecure_cryptography(password):
  salt = b'salt'
  hashed_password = hashlib.md5(salt + password.encode()).hexdigest()

def unsured_variable():
  unused_var = 42

def debug_print():
  print("Debugging information")
