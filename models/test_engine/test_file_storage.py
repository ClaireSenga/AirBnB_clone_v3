#!/usr/bin/python3
"""test file storage"""

import unittest
from models import storage
from models.state import State

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.state = State(name="California")
        storage.new(self.state)
        storage.save()

    def test_get(self):
        """Test get method"""
        obj = storage.get(State, self.state.id)
        self.assertEqual(obj, self.state)

    def test_count(self):
        """Test count method"""
        count = storage.count(State)
        self.assertEqual(count, 1)
        count = storage.count()
        self.assertGreaterEqual(count, 1)

if __name__ == "__main__":
    unittest.main()
