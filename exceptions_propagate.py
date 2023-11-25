# Exception propagation example with user prompt. 

def inner_function(dividend, divisor):
    try:
        # Attempt to perform division
        result = dividend / divisor
        print(result)
    except ZeroDivisionError as e:
        # Handle the error locally in the inner function
        print('Error message managed by inner function: Cannot divide by 0. I will inform my boss (the outer function)')
        # Re-raise the same exception to propagate it to the outer function
        raise


def outer_function():
    while True:  # Keep prompting the user until valid input is provided
        try: 
            # Prompt the user to enter dividend and divisor
            dividend = float(input("Enter the dividend: "))
            divisor = float(input("Enter the divisor: "))
            
            # Call the inner function, which may raise a ZeroDivisionError
            inner_function(dividend, divisor)
        except ZeroDivisionError as e: 
            # Catch the re-raised exception in the outer function
            print('I am the boss (the outer function) being informed of the following error:', e)
            print('Please enter valid values and try again.\n')
        else:
            # If no exception occurred, break out of the loop
            break

# Example usage
# Call the outer function
outer_function()
