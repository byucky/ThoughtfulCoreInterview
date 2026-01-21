"""
Comprehensive test suite for package_sorter module.

Tests cover all three classification categories and various edge cases.
"""

import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    """Test cases for the package sorting function."""
    
    def test_standard_package(self):
        """Test standard packages (not bulky and not heavy)."""
        # Small package, light weight
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
        
        # Medium package, light weight
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        
        # Large package but under volume threshold, light weight
        self.assertEqual(sort(100, 100, 99, 15), "STANDARD")  # 990,000 cm³
        
        # Package with dimensions just under 150 cm but volume under threshold
        self.assertEqual(sort(99, 99, 99, 19), "STANDARD")  # 970,299 cm³
    
    def test_special_package_bulky_only(self):
        """Test special packages that are bulky but not heavy."""
        # Bulky due to volume
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # 1,000,000 cm³
        
        # Bulky due to one dimension >= 150 cm
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 5), "SPECIAL")
        
        # Bulky due to volume > 1,000,000 cm³
        self.assertEqual(sort(100, 100, 101, 10), "SPECIAL")  # 1,010,000 cm³
        
        # Bulky due to dimension exactly 150 cm
        self.assertEqual(sort(150, 149, 149, 19), "SPECIAL")
    
    def test_special_package_heavy_only(self):
        """Test special packages that are heavy but not bulky."""
        # Heavy but small dimensions
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        
        # Heavy but medium dimensions
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        
        # Heavy but just under volume threshold
        self.assertEqual(sort(100, 100, 99, 20), "SPECIAL")  # 990,000 cm³
        
        # Heavy but all dimensions under 150 cm and volume under threshold
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")  # 970,299 cm³
    
    def test_rejected_package(self):
        """Test rejected packages (both heavy and bulky)."""
        # Heavy and bulky due to volume
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")  # 1,000,000 cm³
        
        # Heavy and bulky due to dimension >= 150 cm
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 150, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 10, 150, 20), "REJECTED")
        
        # Heavy and bulky due to both volume and dimension
        self.assertEqual(sort(150, 150, 150, 25), "REJECTED")
        
        # Heavy and bulky - boundary case
        self.assertEqual(sort(150, 149, 149, 20), "REJECTED")
    
    def test_boundary_conditions(self):
        """Test boundary conditions (exactly at thresholds)."""
        # Exactly at volume threshold, not heavy
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")  # 1,000,000 cm³, 19 kg
        
        # Exactly at volume threshold, heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")  # 1,000,000 cm³, 20 kg
        
        # Exactly at dimension threshold, not heavy
        self.assertEqual(sort(150, 10, 10, 19), "SPECIAL")
        
        # Exactly at dimension threshold, heavy
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        
        # Exactly at mass threshold, not bulky
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        
        # Exactly at mass threshold, bulky
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        
        # Just below volume threshold
        self.assertEqual(sort(100, 100, 99, 19), "STANDARD")  # 990,000 cm³
        
        # Just below dimension threshold (but volume makes it bulky)
        # Note: 149×149×149 = 3,307,949 cm³, so it's bulky
        self.assertEqual(sort(149, 149, 149, 19), "SPECIAL")  # Bulky due to volume
        
        # Package with dimension just under 150 and volume under threshold
        self.assertEqual(sort(99, 99, 99, 19), "STANDARD")  # 970,299 cm³
        
        # Just below mass threshold
        self.assertEqual(sort(100, 100, 100, 19.9), "SPECIAL")  # Still bulky
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Very small package
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")
        
        # Very large package (bulky)
        self.assertEqual(sort(200, 200, 200, 10), "SPECIAL")
        
        # Very heavy but small package
        self.assertEqual(sort(1, 1, 1, 50), "SPECIAL")
        
        # Very large and very heavy
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
        
        # Zero dimensions (edge case - mathematically valid but physically unlikely)
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        
        # Floating point values
        self.assertEqual(sort(100.5, 100.5, 100.5, 19.5), "SPECIAL")  # Volume > 1M
        
        # Very large volume
        self.assertEqual(sort(1000, 1000, 1000, 15), "SPECIAL")
        self.assertEqual(sort(1000, 1000, 1000, 25), "REJECTED")
    
    def test_multiple_bulky_conditions(self):
        """Test packages that meet multiple bulky conditions."""
        # Both volume >= 1M and dimension >= 150
        self.assertEqual(sort(150, 100, 100, 10), "SPECIAL")
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")
        
        # Multiple dimensions >= 150
        self.assertEqual(sort(150, 150, 10, 10), "SPECIAL")
        self.assertEqual(sort(150, 150, 10, 20), "REJECTED")


if __name__ == "__main__":
    unittest.main()
