def calculate_sum(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        a, b = 10, 20
    print("Calculator app is running...")
    print(f"Sum = {calculate_sum(a, b)}")
