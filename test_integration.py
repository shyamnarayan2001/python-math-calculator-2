#!/usr/bin/env python3
"""Integration tests for the Python Math Calculator."""

import unittest
import subprocess
import sys
import os
from unittest.mock import patch
from calculator import Calculator
import main


class TestCalculatorIntegration(unittest.TestCase):
    """Integration tests for the complete calculator system."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()
    
    def test_calculator_module_imports(self):
        """Test that all required modules can be imported successfully."""
        try:
            import calculator
            import main
            self.assertTrue(True, "All modules imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import required modules: {e}")
    
    def test_calculator_class_instantiation(self):
        """Test that Calculator class can be instantiated."""
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)
        self.assertTrue(hasattr(calc, 'add'))
        self.assertTrue(hasattr(calc, 'subtract'))
        self.assertTrue(hasattr(calc, 'get_valid_number'))
    
    def test_calculator_methods_callable(self):
        """Test that all calculator methods are callable."""
        calc = Calculator()
        self.assertTrue(callable(calc.add))
        self.assertTrue(callable(calc.subtract))
        self.assertTrue(callable(calc.get_valid_number))
    
    @patch('builtins.input', return_value='5')
    def test_end_to_end_addition_flow(self, mock_input):
        """Test complete addition flow from input to output."""
        calc = Calculator()
        
        # Test input validation
        num1 = calc.get_valid_number("Enter first number: ")
        num2 = calc.get_valid_number("Enter second number: ")
        
        # Test calculation
        result = calc.add(num1, num2)
        
        self.assertEqual(num1, 5.0)
        self.assertEqual(num2, 5.0)
        self.assertEqual(result, 10.0)
    
    @patch('builtins.input', return_value='10')
    def test_end_to_end_subtraction_flow(self, mock_input):
        """Test complete subtraction flow from input to output."""
        calc = Calculator()
        
        # Test input validation
        num1 = calc.get_valid_number("Enter first number: ")
        num2 = calc.get_valid_number("Enter second number: ")
        
        # Test calculation
        result = calc.subtract(num1, num2)
        
        self.assertEqual(num1, 10.0)
        self.assertEqual(num2, 10.0)
        self.assertEqual(result, 0.0)
    
    def test_main_module_functions(self):
        """Test that main module functions exist and are callable."""
        self.assertTrue(hasattr(main, 'main'))
        self.assertTrue(hasattr(main, 'display_menu'))
        self.assertTrue(callable(main.main))
        self.assertTrue(callable(main.display_menu))
    
    def test_calculator_with_various_number_types(self):
        """Test calculator with different number types and ranges."""
        calc = Calculator()
        
        test_cases = [
            (1, 2, 3, -1),           # Small integers
            (100, 50, 150, 50),      # Medium integers  
            (1.5, 2.5, 4.0, -1.0),  # Decimals
            (-5, -3, -8, -2),        # Negative numbers
            (0, 5, 5, -5),           # Zero cases
            (1000000, 999999, 1999999, 1)  # Large numbers
        ]
        
        for num1, num2, expected_add, expected_sub in test_cases:
            with self.subTest(num1=num1, num2=num2):
                add_result = calc.add(num1, num2)
                sub_result = calc.subtract(num1, num2)
                
                self.assertAlmostEqual(add_result, expected_add, places=5)
                self.assertAlmostEqual(sub_result, expected_sub, places=5)
    
    @patch('calculator.Calculator.get_valid_number')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_complete_user_interaction_flow(self, mock_print, mock_input, mock_get_number):
        """Test complete user interaction flow with mocked inputs."""
        # Setup mock returns
        mock_input.side_effect = ['1', '3']  # Addition, then Exit
        mock_get_number.side_effect = [15.5, 4.5]  # Two numbers for addition
        
        # Run main function
        main.main()
        
        # Verify that the calculation was performed and result displayed
        mock_print.assert_any_call("Welcome to the Python Math Calculator!")
        mock_print.assert_any_call("\nAddition Result:")
        mock_print.assert_any_call("15.5 + 4.5 = 20.0")
        mock_print.assert_any_call("Thank you for using the Python Math Calculator!")


class TestSystemCompatibility(unittest.TestCase):
    """Test system compatibility and environment requirements."""
    
    def test_python_version_compatibility(self):
        """Test that the code works with the current Python version."""
        self.assertGreaterEqual(sys.version_info.major, 3)
        self.assertGreaterEqual(sys.version_info.minor, 6)
    
    def test_required_modules_available(self):
        """Test that all required Python modules are available."""
        required_modules = ['unittest', 'sys', 'io']
        
        for module_name in required_modules:
            try:
                __import__(module_name)
            except ImportError:
                self.fail(f"Required module '{module_name}' is not available")
    
    def test_file_structure(self):
        """Test that all required files exist."""
        required_files = ['calculator.py', 'main.py', 'README.md']
        
        for filename in required_files:
            self.assertTrue(os.path.exists(filename), 
                          f"Required file '{filename}' does not exist")


class TestPerformanceAndLimits(unittest.TestCase):
    """Test performance and limit scenarios."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()
    
    def test_large_number_calculations(self):
        """Test calculations with very large numbers."""
        large_num1 = 10**15
        large_num2 = 10**14
        
        add_result = self.calculator.add(large_num1, large_num2)
        sub_result = self.calculator.subtract(large_num1, large_num2)
        
        self.assertEqual(add_result, large_num1 + large_num2)
        self.assertEqual(sub_result, large_num1 - large_num2)
    
    def test_precision_with_many_decimals(self):
        """Test precision with numbers having many decimal places."""
        num1 = 0.123456789012345
        num2 = 0.987654321098765
        
        add_result = self.calculator.add(num1, num2)
        sub_result = self.calculator.subtract(num1, num2)
        
        self.assertAlmostEqual(add_result, num1 + num2, places=10)
        self.assertAlmostEqual(sub_result, num1 - num2, places=10)
    
    def test_repeated_operations(self):
        """Test performing many operations in sequence."""
        calc = Calculator()
        result = 0
        
        # Perform 1000 additions
        for i in range(1000):
            result = calc.add(result, 1)
        
        self.assertEqual(result, 1000)
        
        # Perform 1000 subtractions
        for i in range(1000):
            result = calc.subtract(result, 1)
        
        self.assertEqual(result, 0)


if __name__ == '__main__':
    # Create a test suite combining all test cases
    test_suite = unittest.TestSuite()
    
    # Add all test cases to the suite
    test_suite.addTest(unittest.makeSuite(TestCalculatorIntegration))
    test_suite.addTest(unittest.makeSuite(TestSystemCompatibility))
    test_suite.addTest(unittest.makeSuite(TestPerformanceAndLimits))
    
    # Run the tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print(f"{'='*50}")
