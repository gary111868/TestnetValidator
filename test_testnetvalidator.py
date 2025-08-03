# test_testnetvalidator.py
"""
Tests for TestnetValidator module.
"""

import unittest
from testnetvalidator import TestnetValidator

class TestTestnetValidator(unittest.TestCase):
    """Test cases for TestnetValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TestnetValidator()
        self.assertIsInstance(instance, TestnetValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TestnetValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
