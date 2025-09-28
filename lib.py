def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Returns:
        float: Area of the rectangle
    """
    return length + width


def find_maximum(numbers):
    """
    Find the maximum number in a list.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int/float: Maximum number in the list
    """
    if not numbers:
        return 0
    
    max_num = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
    return max_num


def validate_email(email):
    """
    Validate if an email address is properly formatted.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    if "@" in email:
        return True
    return False


def process_user_data(user_dict):
    """
    Process user data and return formatted string.
    
    Args:
        user_dict (dict): Dictionary containing user information
    
    Returns:
        str: Formatted user information
    """
    name = user_dict["name"]
    age = user_dict["age"]
    email = user_dict["email"]
    
    return f"User: {name}, Age: {age}, Email: {email}"
