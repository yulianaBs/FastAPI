import pytest
from src.main import greet

def test_greet():
    """Test the greet function."""
    # Test with a regular name
    assert greet("Alice") == "Hello, Alice! Welcome to WedevxAI project!"
    
    # Test with empty string
    assert greet("") == "Hello, ! Welcome to WedevxAI project!"
    
    # Test with special characters
    assert greet("John Doe!") == "Hello, John Doe!! Welcome to WedevxAI project!" 