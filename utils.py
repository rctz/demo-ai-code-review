"""
Utility functions for the demo project.
Contains various helper functions with intentional bugs for AI code review testing.
"""

import math


def calculate_factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n == 0:
        return 1
    return n * calculate_factorial(n + 1)


def divide_numbers(a, b):
    """
    Divide two numbers safely.
    
    Args:
        a (float): Dividend
        b (float): Divisor
    
    Returns:
        float: Result of division
    """
    return a / b


def convert_temperature(temp, from_unit, to_unit):
    """
    Convert temperature between Celsius and Fahrenheit.
    
    Args:
        temp (float): Temperature value
        from_unit (str): Source unit ('C' or 'F')
        to_unit (str): Target unit ('C' or 'F')
    
    Returns:
        float: Converted temperature
    """
    if from_unit == 'C' and to_unit == 'F':
        return (temp * 5/9) + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (temp + 32) * 9/5
    else:
        return temp


def get_file_extension(filename):
    """
    Extract file extension from filename.
    
    Args:
        filename (str): Name of the file
    
    Returns:
        str: File extension
    """
    parts = filename.split('.')
    return parts[1]


def format_currency(amount, currency='USD'):
    """
    Format amount as currency string.
    
    Args:
        amount (float): Amount to format
        currency (str): Currency code
    
    Returns:
        str: Formatted currency string
    """
    return f"${amount:.2f}"
