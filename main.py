#!/usr/bin/env python3
"""Main application for the Python Math Calculator."""

from calculator import Calculator

def display_menu():
    """Display the main menu options."""
    print("\n=== Python Math Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    print("================================")

def main():
    """Main function to run the calculator application."""
    calc = Calculator()
    
    print("Welcome to the Python Math Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '3':
                print("Thank you for using the Python Math Calculator!")
                break
            elif choice in ['1', '2']:
                # Get numbers from user
                num1 = calc.get_valid_number("Enter the first number: ")
                num2 = calc.get_valid_number("Enter the second number: ")
                
                if choice == '1':
                    result = calc.add(num1, num2)
                    operation = "Addition"
                    symbol = "+"
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    operation = "Subtraction"
                    symbol = "-"
                
                print(f"\n{operation} Result:")
                print(f"{num1} {symbol} {num2} = {result}")
                
            else:
                print("Invalid choice! Please select 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nExiting calculator. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
