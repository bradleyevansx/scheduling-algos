from collections import deque
from typing import List
from process import Process, displayProcessPropertyInfo, initProcess
from abc import ABC, abstractmethod

class ProcessDispatch:
    def __init__(self, process: Process, timeQuantum: int):
        self.process = process
        self.timeQuantum = timeQuantum

class Scheduler(ABC):
    @abstractmethod
    def tryDispatchProcess(self):
        pass

    @abstractmethod
    def onProcessorTimeIncrease(self, processorTime: int):
        pass

    @abstractmethod
    def hasProcessesLeft(self):
        pass

    @abstractmethod
    def hasProcessessInQueue(self):
        pass

class FCFSScheduler(Scheduler):
    def __init__(self, numberOfProcesses: int):
        self.numberOfProcesses = numberOfProcesses
        self.processes = deque()
        self.q = deque()

    def getProcesses(self):
        displayProcessPropertyInfo()

        for i in range(self.numberOfProcesses):
            self.processes.append(initProcess(i + 1))
    
    def onProcessorTimeIncrease(self, processorTime: int):
        self.passIdleTime()
        while self.hasProcessesLeft() and self.processes[0].arrivalTime <= processorTime:
            self.q.append(self.processes.popleft())

    def hasProcessesLeft(self):
        return len(self.processes) > 0
    
    def hasProcessessInQueue(self):
        return len(self.q) > 0
    
    def tryDispatchProcess(self, processorTime: int):
        if not self.hasProcessessInQueue() or self.q[0].arrivalTime > processorTime:
            return None
        process = self.q.popleft()
        process.timeOfDispatch = processorTime
        processDispatch = ProcessDispatch(process, process.burstTime)
        return processDispatch
    
    def passIdleTime(self):
        for process in self.q:
            process.idleTime += 1



def displayAlogOptions():
    info = """
    Scheduling Algorithm Options:
    -----------------------------------

    1. First Come First Serve (FCFS)
        - Processes are served in the order that they show up to the queue

        | Preemptive | Priority Based | 
        -------------------------------
        |     ❌     |       ❌       |

    2. Shortest Process Next (SPN)
        - Processes are served based on which process has the shortest burst time in the queue

        | Preemptive | Priority Based | 
        -------------------------------
        |     ❌     |       ❌       |

    3. Shortest Remaining Time (SRT)
        - Processes are served based on which process has the shortest amount of time left to be executed in the queue
        - Processes will be allotted a certain amount of CPU time
        
        | Preemptive | Priority Based | 
        -------------------------------
        |     ✅     |       ❌       |

    4. Round Robin (RR)
        - Processes will be served in a circular fashion throughout the queue
        - Processes will be allotted a certain amount of CPU time
        - When the allotted time is used up, if their is time remaining in the process it will be sent to the back of the queue

        | Preemptive | Priority Based | 
        -------------------------------
        |     ✅     |       ❌       |

    5. Priority Scheduling (Non-Preemptive)
        - Processes will be served based on their priority
        - Processes with the same priority will be served on a FCFS basis

        | Preemptive | Priority Based | 
        -------------------------------
        |     ❌     |       ✅       |

    -----------------------------------
"""
    print(info)

def tryGetAlgo():
    value = input(f'Enter the number associated with the algorithm you would like to run: ')
    if value < 1 or value > 5:
        raise Exception("The value you enter must be within 1 <= val <= 5")

def initAlgo():
    # displayAlogOptions()
    # value = tryGetAlgo()
    # print(value)

    return FCFSScheduler