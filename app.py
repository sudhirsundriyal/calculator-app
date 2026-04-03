# app.py
import sys

print("Calculator app is running...")

# Use command line arguments if provided
if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
else:
    a = 10  # default first number
    b = 20  # default second number

print(f"Sum = {a + b}")
