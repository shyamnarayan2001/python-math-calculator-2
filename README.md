# Python Math Calculator

A simple Python calculator application that performs basic math operations (addition and subtraction) on two numbers.

## Features

- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Input Validation**: Handles invalid input gracefully
- **User-Friendly Interface**: Simple command-line menu system
- **Error Handling**: Robust error handling for various scenarios
- **Comprehensive Testing**: Full test suite with unit, integration, and edge case tests

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

## Testing

This project includes a comprehensive test suite with multiple types of tests:

### Running All Tests

```bash
# Run all tests using the test runner
python run_tests.py

# Or run tests using Python's unittest module
python -m unittest discover -v
```

### Running Specific Test Files

```bash
# Run calculator tests only
python test_calculator.py

# Run main module tests only
python test_main.py

# Run integration tests only
python test_integration.py

# Or using the test runner
python run_tests.py test_calculator
```

### Test Coverage

The test suite includes:

- **Unit Tests** (`test_calculator.py`):
  - Basic addition and subtraction operations
  - Input validation and error handling
  - Edge cases (infinity, NaN, very large/small numbers)
  - Floating point precision tests

- **Main Module Tests** (`test_main.py`):
  - Menu display functionality
  - User input handling
  - Exception handling (KeyboardInterrupt, unexpected errors)
  - Integration with Calculator class

- **Integration Tests** (`test_integration.py`):
  - End-to-end workflow testing
  - Module import verification
  - System compatibility checks
  - Performance and limit testing

### Test Results Example

```
======================================================================
TEST SUMMARY
======================================================================
Tests run: 45
Failures: 0
Errors: 0
Skipped: 0
Success rate: 100.0%
======================================================================
```

## Project Structure

```
python-math-calculator-2/
├── calculator.py          # Calculator class with math operations
├── main.py               # Main application with user interface
├── README.md             # Project documentation
├── requirements.txt      # Dependencies (none required)
├── test_calculator.py    # Unit tests for Calculator class
├── test_main.py          # Unit tests for main module
├── test_integration.py   # Integration and system tests
└── run_tests.py          # Test runner script
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

### Testing Files
- `test_calculator.py`: Comprehensive unit tests for the Calculator class
- `test_main.py`: Tests for the main application interface and user interaction
- `test_integration.py`: Integration tests and system compatibility checks
- `run_tests.py`: Unified test runner with detailed reporting

## Development

### Adding New Features

1. Implement the feature in the appropriate module
2. Add comprehensive unit tests
3. Update integration tests if needed
4. Run the full test suite to ensure no regressions
5. Update documentation

### Test-Driven Development

This project follows TDD principles:
1. Write tests first
2. Implement minimal code to pass tests
3. Refactor while maintaining test coverage
4. Ensure all tests pass before committing

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add/update tests as needed
5. Ensure all tests pass (`python run_tests.py`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is open source and available under the MIT License.
