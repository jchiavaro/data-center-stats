import unittest
import sys
sys.path.append("../app/")
from host import Host
from instance import Instance

class TestHost(unittest.TestCase):

    def setUp(self):
        self.h1 = Host(1, 2, 3)
        self.h2 = Host(1, 2, 5)
        self.h3 = Host(4, 2, 5)
        self.hosts = [self.h1, self.h2, self.h3]
        self.i1 = Instance(1, 1, 1)

    def testCreateHost(self):
        newHost = Host(1, 2, 3)
        self.assertIsInstance(newHost, Host)

    def testEquals(self):

        self.assertNotEqual(self.h1, self.h3)
        self.assertEqual(self.h1, self.h2)

    def testAddInstance(self):
        self.h1.addInstance(self.i1)
        self.assertEqual(1, len(self.h1.instances))

if __name__ == '__main__':
    unittest.main()
