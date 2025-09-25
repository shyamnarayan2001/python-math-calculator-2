"""Calculator module for basic math operations."""

class Calculator:
    """A simple calculator class for basic math operations."""
    
    def add(self, num1, num2):
        """Add two numbers and return the result.
        
        Args:
            num1 (float): The first number
            num2 (float): The second number
            
        Returns:
            float: The sum of num1 and num2
        """
        return num1 + num2
    
    def subtract(self, num1, num2):
        """Subtract the second number from the first and return the result.
        
        Args:
            num1 (float): The first number (minuend)
            num2 (float): The second number (subtrahend)
            
        Returns:
            float: The difference of num1 and num2
        """
        return num1 - num2

    def get_valid_number(self, prompt):
        """Get a valid number from user input.
        
        Args:
            prompt (str): The prompt to display to the user
            
        Returns:
            float: A valid number entered by the user
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
