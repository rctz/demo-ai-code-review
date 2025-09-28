"""
Main application file demonstrating usage of various modules.
This file imports and uses functions from lib.py, utils.py, data_processor.py, and config.py.
"""

from lib import calculate_area, find_maximum, validate_email, process_user_data
from utils import calculate_factorial, divide_numbers, convert_temperature, get_file_extension, format_currency
from data_processor import DataProcessor
from config import Config, get_log_level


def test_lib_functions():
    """Test functions from lib.py module."""
    print("=== Testing lib.py functions ===")
    
    area = calculate_area(5, 3)
    print(f"Area of rectangle (5x3): {area}")
    
    numbers = [1, 5, 3, 9, 2]
    max_num = find_maximum(numbers)
    print(f"Maximum in {numbers}: {max_num}")
    
    empty_max = find_maximum([])
    print(f"Maximum in empty list: {empty_max}")
    
    email1 = "test@example.com"
    email2 = "invalid_email"
    print(f"Is '{email1}' valid? {validate_email(email1)}")
    print(f"Is '{email2}' valid? {validate_email(email2)}")
    
    user = {"name": "John", "age": 30, "email": "john@example.com"}
    user_info = process_user_data(user)
    print(f"User info: {user_info}")


def test_utils_functions():
    """Test functions from utils.py module."""
    print("\n=== Testing utils.py functions ===")
    
    try:
        factorial = calculate_factorial(5)
        print(f"Factorial of 5: {factorial}")
    except RecursionError:
        print("RecursionError occurred in factorial calculation")
    
    try:
        result = divide_numbers(10, 2)
        print(f"10 / 2 = {result}")
        result_zero = divide_numbers(10, 0)
        print(f"10 / 0 = {result_zero}")
    except ZeroDivisionError:
        print("Division by zero error occurred")
    
    celsius_to_fahrenheit = convert_temperature(0, 'C', 'F')
    fahrenheit_to_celsius = convert_temperature(32, 'F', 'C')
    print(f"0°C to Fahrenheit: {celsius_to_fahrenheit}°F")
    print(f"32°F to Celsius: {fahrenheit_to_celsius}°C")
    
    try:
        ext1 = get_file_extension("document.pdf")
        ext2 = get_file_extension("no_extension")
        print(f"Extension of 'document.pdf': {ext1}")
        print(f"Extension of 'no_extension': {ext2}")
    except IndexError:
        print("IndexError occurred in file extension extraction")
    
    formatted = format_currency(123.456)
    print(f"Formatted currency: {formatted}")


def test_data_processor():
    """Test DataProcessor class."""
    print("\n=== Testing data_processor.py ===")
    
    processor = DataProcessor()
    
    try:
        avg1 = processor.calculate_average([1, 2, 3, 4, 5])
        print(f"Average of [1,2,3,4,5]: {avg1}")
        avg2 = processor.calculate_average([])
        print(f"Average of empty list: {avg2}")
    except ZeroDivisionError:
        print("Division by zero error in average calculation")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_nums = processor.filter_even_numbers(numbers)
    print(f"Even numbers from {numbers}: {even_nums}")
    
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    print(f"Dict1 before merge: {dict1}")
    merged = processor.merge_dictionaries(dict1, dict2)
    print(f"Merged dict: {merged}")
    print(f"Dict1 after merge: {dict1}")
    
    valid_data = [1, 2.5, "hello", True]
    invalid_data = [1, [2, 3], {"key": "value"}]
    print(f"Valid data types for {valid_data}: {processor.validate_data_types(valid_data)}")
    print(f"Valid data types for {invalid_data}: {processor.validate_data_types(invalid_data)}")


def test_config():
    """Test Config class."""
    print("\n=== Testing config.py ===")
    
    config = Config()
    
    try:
        debug_setting = config.get_setting('debug')
        nonexistent = config.get_setting('nonexistent_key')
        print(f"Debug setting: {debug_setting}")
        print(f"Nonexistent setting: {nonexistent}")
    except KeyError:
        print("KeyError occurred when accessing nonexistent setting")
    
    is_valid = config.validate_config()
    print(f"Configuration is valid: {is_valid}")
    
    db_url = config.get_database_url()
    print(f"Database URL: {db_url}")
    
    log_level = get_log_level()
    print(f"Log level: {log_level}")


def main():
    """Main function to run all tests."""
    print("Starting AI Code Review Demo")
    print("This project contains intentional bugs for testing AI code review tools")
    print("=" * 60)
    
    test_lib_functions()
    test_utils_functions()
    test_data_processor()
    test_config()
    
    print("\n" + "=" * 60)
    print("Demo completed. Check the code for various types of bugs!")


if __name__ == "__main__":
    main()
