import random
import string
from datetime import datetime


def generate_random_name(prefix=""):
    """
    Generate a random name with timestamp for uniqueness.
    
    Args:
        prefix (str): Prefix for the name
        
    Returns:
        str: Generated unique name
    """
    timestamp = datetime.now().strftime("%H%M%S")
    random_suffix = ''.join(random.choices(string.ascii_letters, k=3))
    return f"{prefix}{timestamp}{random_suffix}" if prefix else timestamp + random_suffix


def generate_employee_name(first_name="John", last_name="Doe"):
    """
    Generate unique employee names with timestamp for uniqueness.
    
    Args:
        first_name (str): First name prefix
        last_name (str): Last name prefix
        
    Returns:
        tuple: (first_name, last_name) unique combination
    """
    timestamp = datetime.now().strftime("%H%M%S")
    return f"{first_name}{timestamp}", f"{last_name}{timestamp}"
