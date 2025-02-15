from abc import ABC, abstractmethod
import re

def displayProcessPropertyInfo():
    info = """
    Process Properties Information:
    --------------------------------

    1. Arrival Time:
       - Description: The time at which the process will arrive in the queue.
       - Constraints: Integer >= 1
       - Default Value: 1

    2. Burst Time:
       - Description: The amount of time needed for the process to execute.
       - Constraints: Integer >= 1
       - Default Value: 1

    3. Priority:
       - Description: The priority of the process in the queue.
       - Constraints: Integer value p where 1 <= p <= 5
       - Default Value: 1 (1 is the lowest priority, 5 is the highest)

    --------------------------------
    """
    print(info)


class ProcessProperty(ABC):
    def setValue(self, value: str):
        if self.validateProperty(value):
            self.value = value
        else:
            raise Exception('The value you enter must conform to the constraints that you were provided with')
        self.value = int(value)
    
    @abstractmethod
    def validateProperty(self, value: str):
        pass

    def requestValue(self, processId: int):
        value = input(f'Enter process {processId}\'s {self.getFormattedName()}: ')
        self.setValue(value)

    def getFormattedName(self):
        return ' '.join([word for word in re.findall('[A-Z][a-z]*', self.__class__.__name__)])


class ArrivalTime(ProcessProperty):
    def validateProperty(self, value: str):
        if len(value) == 0 or not value.isdigit() or int(value) < 1:
            return False
        return True

class BurstTime(ProcessProperty):
    def validateProperty(self, value: str):
        if len(value) == 0 or not value.isdigit() or int(value) < 1:
            return False
        return True

class Priority(ProcessProperty):    
    def validateProperty(self, value: str):
        if len(value) == 0 or not value.isdigit() or int(value) < 1 or int(value) > 5:
            return False
        return True
        
class Process:
   def __init__(self, id: int, arrivalTime: int, burstTime: int, priority: int):
        self.id = id
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.timeRemaining = burstTime
        self.priority = priority  
        self.idleTime = 0

def initProcess(processId: int, requestPriority: bool = False):
    unprocessProperties = ProcessProperty.__subclasses__()
    if not requestPriority:
        unprocessProperties = filter(lambda x: x != Priority, unprocessProperties)
    properties = []

    for property in unprocessProperties:
        propIntance = property()
        propIntance.requestValue(processId)
        properties.append(propIntance)
    
    return Process(processId, properties[0].value, properties[1].value, properties[2].value if requestPriority else 1)