import unittest
import sys
sys.path.append("../app/")
from host import Host
from instance import Instance
from statistics_service import StatisticsService
from data_reader import DataReader
from sets import Set

class TestStatisticsServie(unittest.TestCase):

    def setUp(self):
       DataReader.createHostsFromFile()
       DataReader.createInstancesFromFile()

    def tearDown(self):
       DataReader.instances = []
       DataReader.hosts = []

    def testGetMaxCustomerFleetForHost(self):
        totalFleet = StatisticsService.getMaxCustomerFleetForHost(2, 8)
        self.assertEqual(totalFleet, 19)

        totalFleet = StatisticsService.getMaxCustomerFleetForHost(9, 16)
        self.assertEqual(totalFleet, 9)

    def testGetMaxCustomerFleetForDatacentre(self):
        totalFleet = StatisticsService.getMaxCustomerFleetForDatacentre(2, 8)
        self.assertEqual(totalFleet, 4)

        totalFleet = StatisticsService.getMaxCustomerFleetForDatacentre(1, 16)
        self.assertEqual(totalFleet, 3)

    def testGetHostsWithEmptySlots(self):
        emptyHosts = StatisticsService.getHostsWithEmptySlots()
        self.assertSetEqual(emptyHosts, set([10]))

if __name__ == '__main__':
    unittest.main()
