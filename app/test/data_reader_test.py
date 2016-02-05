import unittest
import sys
sys.path.append("../app/")
from data_reader import DataReader
from instance import Instance
from host import Host

class TestDataReader(unittest.TestCase):
    TEST_HOSTS_FILE = 'test/testHosts.txt'
    TEST_INSTANCES_FILE = 'test/testInstances.txt'

    def testCreateHostsFromFile(self):
         DataReader.createHostsFromFile(TestDataReader.TEST_HOSTS_FILE)
         self.assertEquals(len(DataReader.hosts), 8)

    def testCreateHostsFileError(self):
         DataReader.createHostsFromFile(TestDataReader.TEST_HOSTS_FILE)
         self.assertRaises(Exception)

    def testFindHostByID(self):
        host = DataReader.findHostByID(2)
        self.assertIsNotNone(host)

        host = DataReader.findHostByID(-1)
        self.assertIsNone(host)

    def testCreateInstancesFromFile(self):
        DataReader.createInstancesFromFile(TestDataReader.TEST_INSTANCES_FILE)
        self.assertEquals(len(DataReader.instances), 15)
        for i in DataReader.instances:
            self.assertIsNotNone(i.host)

if __name__ == '__main__':
    unittest.main()
