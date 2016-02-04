class DataReader:
    HOSTS_FILE = 'HostState.txt'
    INSTANCES_FILE = 'InstanceState.txt'
    hosts = []

    def __init__(self):
        #self.hosts = []
        self.instances = []

    def __getRows(self, fileName):
        rows = []
        with open(fileName, 'r') as f:
            data = f.readlines()
            for line in data:
                row = line.split(',')
                #validate and log row length
                rows.append(row)
        return rows

    def createHosts(self):
        for host in __getRows(HOSTS_FILE):
            hosts.append(Host(host[0], host[1], host[2]))

    def createInstances(self):
        for instRow in __getRows(INSTANCES_FILE):
            hostCriteria = Host(instance.hostID)
            host = Host.findHost(hostCriteria)
            host.addInstance(instance)
            instance = Instance(instRow[0], instRow[1], instRow[2])
            instance.setHost(host)
            self.instances.append(instance)

    @staticmethod
    def findHost(host):
        if host in hosts:
            return host
        return None
