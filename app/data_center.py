#!/usr/bin/python

import argparse
from data_reader import DataReader
from stats_writer import StatsWriter
import sys
import logging

STATS_FILE = 'statistics.txt'
LOG_FORMAT = '%(asctime)-15s %(message)s'

def setup():
    logging.basicConfig(format=LOG_FORMAT, filename='datacentre.log', level=logging.DEBUG)

def initData(hfile, ifile):
    setup()
    logging.info('INITIALIZING DATA: Reading host and instance files')
    DataReader.createHostsFromFile(hfile)
    DataReader.createInstancesFromFile(ifile)

def run(hfile, ifile, sfile, customerID, hostID, datacentreID):
    initData(hfile, ifile)
    StatsWriter.writeStatistics(sfile, customerID, hostID, datacentreID)

def main():
    parser = argparse.ArgumentParser(description = 'Calculate statistics for hosts and customers')
    parser.add_argument("customer", help="The customerID for statistics - i.e: 3", type=int)
    parser.add_argument("host", help="The hostID for statistics - i.e: 8", type=int)
    parser.add_argument("datacentre", help="The datacentreID for statistics - i.e: 1", type=int)
    parser.add_argument("-f", "--hostsfile", help="Read data from the hosts file: i.e: hosts.txt", default='HostState.txt')
    parser.add_argument("-i", "--instancesfile", help="Read data from the instances file - i.e: instances.txt", default='InstanceState.txt')
    parser.add_argument("-s", "--sfile", help="Write statistics data to the specified file - i.e: statistics.txt", default='statistics.txt')

    args = parser.parse_args()

    try:
        run(args.hostsfile, args.instancesfile, args.sfile, args.customer, args.host, args.datacentre)
    except Exception as e:
        logging.error('SYSTEM ERROR: ' + e.message)
        print 'Error parsing files: Fix the input data files and try again.'
        sys.exit(1)

if __name__ == "__main__":
    main()
