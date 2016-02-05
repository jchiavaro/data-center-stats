import unittest
import sys
sys.path.append("../app/")
from stats_writer import StatsWriter
from data_reader import DataReader
import os.path

class TestStatsWriter(unittest.TestCase):
    STATISTICS_FILE = 'test/testStatistics.txt'

    def setUp(self):
       DataReader.createHostsFromFile()
       DataReader.createInstancesFromFile()

    def tearDown(self):
       DataReader.instances = []
       DataReader.hosts = []

    def testWriteStatistics(self):
        StatsWriter.writeStatistics(TestStatsWriter.STATISTICS_FILE, 8, 2, 0)
        self.assertTrue(os.path.exists(TestStatsWriter.STATISTICS_FILE))

if __name__ == '__main__':
    unittest.main()
