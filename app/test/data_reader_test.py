import unittest
import sys
sys.path.append("../app/")
from host import Host
from instance import Instance

class TestDataReader(unittest.TestCase):

    def setUp(self):
        self.h1 = Host(1, 2, 3)
        self.h2 = Host(1, 2, 5)
        self.h3 = Host(4, 2, 5)
        self.hosts = [self.h1, self.h2, self.h3]
        self.i1 = Instance(1, 1, 1)

    def testFindHost(self):

if __name__ == '__main__':
    unittest.main()
