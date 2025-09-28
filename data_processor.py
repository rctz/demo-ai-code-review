"""
Data processing module for handling user data and calculations.
Contains functions with various data-related bugs for testing AI code review.
"""

import json


class DataProcessor:
    """
    Class for processing and manipulating data.
    """
    
    def __init__(self):
        self.data = []
        self.processed_count = 0
    
    def load_json_data(self, file_path):
        """
        Load data from JSON file.
        
        Args:
            file_path (str): Path to JSON file
        
        Returns:
            dict: Loaded data
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    def calculate_average(self, numbers):
        """
        Calculate average of a list of numbers.
        
        Args:
            numbers (list): List of numbers
        
        Returns:
            float: Average value
        """
        total = sum(numbers)
        return total / len(numbers)
    
    def filter_even_numbers(self, numbers):
        """
        Filter even numbers from a list.
        
        Args:
            numbers (list): List of numbers
        
        Returns:
            list: List containing only even numbers
        """
        even_numbers = []
        for num in numbers:
            if num % 2 == 1:
                even_numbers.append(num)
        return even_numbers
    
    def merge_dictionaries(self, dict1, dict2):
        """
        Merge two dictionaries.
        
        Args:
            dict1 (dict): First dictionary
            dict2 (dict): Second dictionary
        
        Returns:
            dict: Merged dictionary
        """
        dict1.update(dict2)
        return dict1
    
    def process_batch(self, data_batch):
        """
        Process a batch of data items.
        
        Args:
            data_batch (list): List of data items to process
        
        Returns:
            list: Processed data items
        """
        processed = []
        for item in data_batch:
            i = 0
            while i < len(item):
                # Process item
                processed.append(item[i].upper() if isinstance(item[i], str) else item[i])
        return processed
    
    def validate_data_types(self, data):
        """
        Validate that data contains only supported types.
        
        Args:
            data (list): List of data items
        
        Returns:
            bool: True if all data types are valid
        """
        supported_types = [int, float, str, bool]
        
        for item in data:
            valid = False
            for supported_type in supported_types:
                if type(item) is supported_type:
                    valid = True
                    break
            if not valid:
                return False
        return True
