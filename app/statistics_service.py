from host import Host
from instance import Instance
from data_reader import DataReader
from sets import Set
import logging

class StatisticsService:

    @staticmethod
    def getMaxCustomerFleetForHost(hostID, customerID):
        """Returns the customer with the largest fraction of their total fleet of instancehte s on a single host"""

        logging.info('STATISTICS: Calculating customer fleet per host')
        totalFleet = sum(i.host.numberOfSlots for i in DataReader.instances if i.customerID == customerID and i.host is not None)
        return totalFleet

    @staticmethod
    def getMaxCustomerFleetForDatacentre(datacentreID, customerID):
        """Returns the customer with the largest fraction of their total fleet of instances in a single datacentre"""

        logging.info('STATISTICS: Calculating customer fleet per datacentre')
        totalFleet = sum(i.host.numberOfSlots for i in DataReader.instances if i.customerID == customerID and i.host.datacentreID == datacentreID)
        return totalFleet

    @staticmethod
    def getHostsWithEmptySlots():
        """Returns a list of all the hosts which have at least one empty slot"""

        logging.info('STATISTICS: Calculating free clusters')
        hosts = set([h.hostID for h in DataReader.hosts])
        instances = set([i.hostID for i in DataReader.instances])
        return hosts - instances

