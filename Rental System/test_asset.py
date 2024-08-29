import unittest
import datetime
from main import Asset



class TestAsset(unittest.TestCase):

    def test_asset_class_exists(self):
        asset = Asset(1, "Laptop", "Hardware", datetime.date(2023, 7, 15), 2, True)
        self.assertIsInstance(asset, Asset)

    def test_islower(self):
        self.assertTrue('q'.islower())
        self.assertFalse('Q'.islower())
        

    @unittest.skip("skipping")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "not good")
    def test_skipirf(self):
        pass