# test_flexledger.py
"""
Tests for FlexLedger module.
"""

import unittest
from flexledger import FlexLedger

class TestFlexLedger(unittest.TestCase):
    """Test cases for FlexLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FlexLedger()
        self.assertIsInstance(instance, FlexLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FlexLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
