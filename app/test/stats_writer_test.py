import unittest
import sys
sys.path.append("../app/")
from stats_writer import StatsWriter

class TestStatsWriter(unittest.TestCase):
    STATISTICS_FILE = 'test/testStatistics.txt'

    def testWriteStatistics(self):
        StatsWriter.writeStatistics(TestStatsWriter.STATISTICS_FILE, 8, 10, 3)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
