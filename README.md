# Python Math Calculator

A simple Python calculator application that performs basic math operations (addition and subtraction) on two numbers.

## Features

- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Input Validation**: Handles invalid input gracefully
- **User-Friendly Interface**: Simple command-line menu system
- **Error Handling**: Robust error handling for various scenarios

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/shyamnarayan2001/python-math-calculator-2.git
   cd python-math-calculator-2
   ```

## Usage

1. Run the calculator:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu:
   - Choose `1` for Addition
   - Choose `2` for Subtraction
   - Choose `3` to Exit

3. Enter your numbers when prompted and see the results!

## Example

```
=== Python Math Calculator ===
1. Addition
2. Subtraction
3. Exit
================================
Enter your choice (1-3): 1
Enter the first number: 10
Enter the second number: 5

Addition Result:
10.0 + 5.0 = 15.0
```

## Project Structure

```
python-math-calculator-2/
├── calculator.py    # Calculator class with math operations
├── main.py         # Main application with user interface
└── README.md       # Project documentation
```

## Code Structure

### calculator.py
Contains the `Calculator` class with methods for:
- `add(num1, num2)`: Addition operation
- `subtract(num1, num2)`: Subtraction operation
- `get_valid_number(prompt)`: Input validation helper

### main.py
Main application that:
- Provides a user-friendly menu interface
- Handles user input and choice selection
- Displays results in a clear format
- Includes error handling and graceful exit

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.
