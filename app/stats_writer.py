from statistics_service import StatisticsService
import logging

class StatsWriter:

    @staticmethod
    def writeStatistics(fileName, customerID, hostID, datacentreID):
        logging.info('STATISTICS: Generating statistics file')
        totalCustomerHost = StatisticsService.getMaxCustomerFleetForHost(hostID, customerID)
        totalCustomerDatacentre = StatisticsService.getMaxCustomerFleetForDatacentre(datacentreID, customerID)
        freeHosts = StatisticsService.getHostsWithEmptySlots()
        freeHostsLine = ''
        for i in freeHosts:
            freeHostsLine += str(i) + ','
        if len(freeHostsLine) > 0:
                freeHostsLine = freeHostsLine[:-1]
        else:
            freeHostsLine = '0\n'
            logging.info('STATISTICS: No free hosts available')
        with open(fileName, 'w') as f:
            f.write('STATISTICS CLUSTERS INFO\n')
            f.write('------------------------\n')
            f.write('HostClustering: ' + str(customerID) + ',' + str(totalCustomerHost) + '\n')
            f.write('DatacentreClustering: ' + str(customerID) + ',' + str(totalCustomerDatacentre) + '\n')
            f.write('AvailableHosts: ' + str(freeHostsLine) + '\n')

