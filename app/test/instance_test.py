import unittest
import sys
sys.path.append("../app/")
from host import Host
from instance import Instance

class TestInstance(unittest.TestCase):

    def setUp(self):
        self.i1 = Instance(1, 2, 3)
        self.i2 = Instance(1, 2, 5)
        self.i3 = Instance(4, 2, 5)
        self.i1 = Instance(1, 1, 1)
        self.host = Host(1, 2, 3)

    def testCreateInstance(self):
        newInstance = Instance(1, 2, 3)
        self.assertIsInstance(newInstance, Instance)

    def testEquals(self):
        self.assertNotEqual(self.i1, self.i3)
        self.assertEqual(self.i1, self.i2)

    def testSetHost(self):
        self.i1.setHost(self.host)
        self.assertIsNotNone(self.i1.host)

if __name__ == '__main__':
    unittest.main()
