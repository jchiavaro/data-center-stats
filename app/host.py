class Host:
    def __init__(self, hostID, numberOfSlots, datacentreID):
        self.hostID = hostID
        self.numberOfSlots = numberOfSlots
        self.datacentreID = datacentreID
        self.instances = []

    def addInstance(self, instance):
        self.instances.append(instance)

    def __eq__ (self, other):
        return self.hostID == other.hostID
