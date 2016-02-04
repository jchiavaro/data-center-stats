from statistics_service import StatisticsService

class StatsWriter:

    @staticmethod
    def writeStatistics(fileName, customerID, hostID, datacentreID):
        totalCustomerHost = StatisticsService.getMaxCustomerFleetForHost(hostID, customerID)
        totalCustomerDatacentre = StatisticsService.getMaxCustomerFleetForDatacentre(datacentreID, customerID)
        freeHosts = StatisticsService.getHostsWithEmptySlots()
        freeHostsLine = ''
        for i in freeHosts:
            print i
            freeHostsLine += str(i) + ','
        if len(freeHostsLine) > 0:
            freeHostsLine.replace(freeHostsLine[-1], '\n')
        else:
            freeHostsLine = '0\n'
        print freeHostsLine
        with open(fileName, 'w') as f:
            f.write('STATISTICS CLUSTERS INFO\n')
            f.write('------------------------\n')
            f.write('HostClustering: ' + str(customerID) + ',' + str(totalCustomerHost) + '\n')
            f.write('DatacentreClustering: ' + str(customerID) + ',' + str(totalCustomerDatacentre) + '\n')
            f.write('AvailableHosts: ' + str(freeHostsLine))

