# test_codeqlquery.py
"""
Tests for CodeQLQuery module.
"""

import unittest
from codeqlquery import CodeQLQuery

class TestCodeQLQuery(unittest.TestCase):
    """Test cases for CodeQLQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodeQLQuery()
        self.assertIsInstance(instance, CodeQLQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodeQLQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
