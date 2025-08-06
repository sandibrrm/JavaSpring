# test_javaspring.py
"""
Tests for JavaSpring module.
"""

import unittest
from javaspring import JavaSpring

class TestJavaSpring(unittest.TestCase):
    """Test cases for JavaSpring class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JavaSpring()
        self.assertIsInstance(instance, JavaSpring)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JavaSpring()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
