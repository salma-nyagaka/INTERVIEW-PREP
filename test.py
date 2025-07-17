def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both arguments must be numbers!")
        return None
    else:
        # Only runs if no exception occurred
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed.")

# Usage
print(safe_divide(10, 2))   # Success case
print(safe_divide(10, 0))   # ZeroDivisionError case
print(safe_divide(10, "2")) # TypeError case