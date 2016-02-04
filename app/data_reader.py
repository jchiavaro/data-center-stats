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
                if not len(rows) == 3:
                    raise(Exception('Invalid Row length'))
                    logging.error('FILE FORMAT ERROR: Invalid line')
                rows.append(row)
        return rows

    @staticmethod
    def createHostsFromFile(fileName = None):
        if fileName == None:
            fileName = DataReader.HOSTS_FILE
        for host in DataReader.__getRows(fileName):
            host = Host(int(host[0]), int(host[1]), int(host[2]))
            if host not in DataReader.hosts:
                DataReader.hosts.append(host)
            else:
                logging.info('DUPLICATED HOST: skipping host')


    @staticmethod
    def findHostByID(hostID):
        result = [h for h in DataReader.hosts if h.hostID == hostID]
        if len(result) == 1:
            return result[0]
        elif len(result) > 1:
            logging.error('FIND HOST: Duplicated host')
            raise(Exception('Duplicated host'))
        else:
            logging.info('FIND HOST: Host not found')
            raise(Exception('Host not found'))

    @staticmethod
    def createInstancesFromFile(fileName = None):
        if fileName == None:
            fileName = DataReader.INSTANCES_FILE
        for instRow in DataReader.__getRows(fileName):
            instance = Instance(int(instRow[0]), int(instRow[1]), int(instRow[2]))
            try:
                host = DataReader.findHostByID(instance.hostID)
            except Exception as e:
                logging.error('CREATE INSTANCE: Orphan instance')
            if host is not None:
                instance.setHost(host)
                host.addInstance(instance)
            DataReader.instances.append(instance)

    @staticmethod
    def findHost(host):
        if host in hosts:
            return host
        return None
