class Instance:
    def __init__(self, instanceID, customerID, hostID):
        self.instanceID = instanceID
        self.customerID = customerID
        self.hostID = hostID
        self.instances = []
        self.host = None

    def setHost(self, host):
        self.host = host

    def __eq__ (self, other):
        return self.instanceID == other.instanceID
