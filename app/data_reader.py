from host import Host
from instance import Instance
import logging

class DataReader:
    HOSTS_FILE = 'HostState.txt'
    INSTANCES_FILE = 'InstanceState.txt'
    hosts = []
    instances = []

    @staticmethod
    def __getRows(fileName):
        rows = []
        with open(fileName, 'r') as f:
            data = f.readlines()
            for line in data:
                row = line.split(',')
                if len(row) != 3:
                    raise(Exception('Invalid Row length'))
                    logging.error('FILE FORMAT ERROR: Invalid line')
                rows.append(row)
        return rows

    @staticmethod
    def createHostsFromFile(fileName = None):
        if fileName == None:
            fileName = DataReader.HOSTS_FILE
        try:
            allRows = DataReader.__getRows(fileName)
        except Exception as e:
            logging.error('FILE ERROR: ' + e.message)
            raise(e)
        for host in allRows:
            host = Host(int(host[0]), int(host[1]), int(host[2]))
            if host not in DataReader.hosts:
                logging.debug('DATA READER: Adding host ' + str(host.hostID))
                DataReader.hosts.append(host)
            else:
                logging.info('DUPLICATED HOST: skipping host')

    @staticmethod
    def createInstancesFromFile(fileName = None):
        if fileName == None:
            fileName = DataReader.INSTANCES_FILE
        for instRow in DataReader.__getRows(fileName):
            instance = Instance(int(instRow[0]), int(instRow[1]), int(instRow[2]))
            host = DataReader.findHostByID(instance.hostID)
            if host is not None:
                instance.setHost(host)
                host.addInstance(instance)
            else:
                logging.error('CREATE INSTANCE: Orphan instance - Skipping instance')
                continue
            logging.debug('DATA READER: Adding instance ' + str(instance.hostID))
            DataReader.instances.append(instance)

    @staticmethod
    def findHostByID(hostID):
        result = [h for h in DataReader.hosts if h.hostID == hostID]
        if len(result) == 1:
            return result[0]
        elif len(result) > 1:
            logging.error('FIND HOST: Duplicated host')
            return None
        else:
            logging.info('FIND HOST: Host not found')
            return None
