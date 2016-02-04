from host import Host
from instance import Instance
from data_reader import DataReader
from sets import Set

class StatisticsService:

    @staticmethod
    def getMaxCustomerFleetForHost(hostID, customerID):
        totalFleet = sum(i.host.numberOfSlots for i in DataReader.instances if i.customerID == customerID and i.host is not None)
        return totalFleet

    @staticmethod
    def getMaxCustomerFleetForDatacentre(datacentreID, customerID):
        totalFleet = sum(i.host.numberOfSlots for i in DataReader.instances if i.customerID == customerID and i.host.datacentreID == datacentreID)
        return totalFleet

    @staticmethod
    def getHostsWithEmptySlots():
        hosts = set([h.hostID for h in DataReader.hosts])
        instances = set([i.hostID for i in DataReader.instances])
        return hosts - instances

