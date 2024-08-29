import unittest
import datetime
from main import Asset



class TestAsset(unittest.TestCase):
    
    def test_init_valid_data_laptop(self):
        """Test Asset object initialization with valid data."""
        asset = Asset(1, "Laptop", "Hardware", datetime.date(2023, 7, 15), 2, True)
        self.assertEqual(asset.asset_id, 1)
        self.assertEqual(asset.name, "Laptop")
        self.assertEqual(asset.type, "Hardware")
        self.assertEqual(asset.purchase_date, datetime.date(2023, 7, 15))
        self.assertEqual(asset.asset_quantity, 2)
        self.assertTrue(asset.availability)
    
    def test_init_valid_data_mouse(self):
        """Test Asset object initialization with valid data."""
        asset = Asset(2, "Mouse", "Hardware", datetime.date(2024, 1, 1), 2, True)
        self.assertEqual(asset.asset_id, 3)
        self.assertEqual(asset.name, "Mouse")
        self.assertEqual(asset.type, "Hardware")
        self.assertEqual(asset.purchase_date, datetime.date(2024, 1, 1))
        self.assertEqual(asset.asset_quantity, 2)
        self.assertTrue(asset.availability)

    @unittest.skip("skipping")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "not good")
    def test_skipirf(self):
        pass