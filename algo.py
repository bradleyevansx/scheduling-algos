from collections import deque
import heapq
from typing import Optional
from process import Process, displayProcessPropertyInfo, initProcess
from abc import ABC, abstractmethod

from visual import Visualizer


class ProcessDispatch:
    def __init__(self, process: Process, timeQuantum: int):
        self.process = process
        self.timeQuantum = timeQuantum


class Scheduler(ABC):
    @abstractmethod
    def tryDispatchProcess(self, processorTime: int) -> Optional[ProcessDispatch]:
        pass

    @abstractmethod
    def onProcessorTimeIncrease(self, processorTime: int):
        pass

    @abstractmethod
    def hasProcessesLeft(self) -> bool:
        pass

    @abstractmethod
    def hasProcessessInQueue(self) -> bool:
        pass

    @abstractmethod
    def enqueueProcesses(self, processorTime: int) -> None:
        pass


class FCFSScheduler(Scheduler):
    def __init__(self, numberOfProcesses: int, visualizer: Visualizer):
        self.numberOfProcesses = numberOfProcesses
        self.processes = []
        self.q = deque()
        self.visualizer = visualizer

    def getProcesses(self):
        displayProcessPropertyInfo()

        for i in range(self.numberOfProcesses):
            self.processes.append(initProcess(i + 1))
        self.processes.sort(key=lambda p: p.arrivalTime)
        self.processes = deque(self.processes)

    def enqueueProcesses(self, processorTime: int):
        while (
            self.hasProcessesLeft() and self.processes[0].arrivalTime <= processorTime
        ):
            self.q.append(self.processes.popleft())

    def onProcessorTimeIncrease(self, processorTime: int):
        self.passIdleTime(processorTime - 1)
        self.enqueueProcesses(processorTime)

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

    def passIdleTime(self, processorTime: int):
        for process in self.q:
            processId = process.id
            self.visualizer.trackProcessAction(processId, processorTime, "W")
            process.idleTime += 1


class SPNScheduler(Scheduler):
    def __init__(self, numberOfProcesses: int, visualizer: Visualizer):
        self.numberOfProcesses = numberOfProcesses
        self.processes = []
        self.q = []
        self.visualizer = visualizer

    def getProcesses(self):
        displayProcessPropertyInfo()

        for i in range(self.numberOfProcesses):
            self.processes.append(initProcess(i + 1))
        self.processes.sort(key=lambda p: p.arrivalTime)
        self.processes = deque(self.processes)

    def enqueueProcesses(self, processorTime: int):
        while (
            self.hasProcessesLeft() and self.processes[0].arrivalTime <= processorTime
        ):
            newProcess = self.processes.popleft()
            heapq.heappush(
                self.q,
                (
                    newProcess.burstTime,
                    newProcess.arrivalTime,
                    newProcess.id,
                    newProcess,
                ),
            )

    def onProcessorTimeIncrease(self, processorTime: int):
        self.passIdleTime(processorTime - 1)
        self.enqueueProcesses(processorTime)

    def hasProcessesLeft(self):
        return len(self.processes) > 0

    def hasProcessessInQueue(self):
        return len(self.q) > 0

    def tryDispatchProcess(self, processorTime: int):
        if not self.hasProcessessInQueue() or self.q[0][3].arrivalTime > processorTime:
            return None
        burstTime, _, _, process = heapq.heappop(self.q)
        process.timeOfDispatch = processorTime
        processDispatch = ProcessDispatch(process, burstTime)
        return processDispatch

    def passIdleTime(self, processorTime):
        for process in self.q:
            processId = process[2]
            self.visualizer.trackProcessAction(processId, processorTime, "W")
            process[3].idleTime += 1


class SRTScheduler(Scheduler):
    def __init__(self, numberOfProcesses: int, visualizer: Visualizer):
        self.numberOfProcesses = numberOfProcesses
        self.processes = []
        self.q = []
        self.timeQuantum = 1
        self.visualizer = visualizer

    def getProcesses(self):
        displayProcessPropertyInfo()

        for i in range(self.numberOfProcesses):
            self.processes.append(initProcess(i + 1))
        self.processes.sort(key=lambda p: p.arrivalTime)
        self.processes = deque(self.processes)

    def enqueueProcesses(self, processorTime: int):
        while (
            self.hasProcessesLeft() and self.processes[0].arrivalTime <= processorTime
        ):
            newProcess = self.processes.popleft()
            heapq.heappush(
                self.q,
                (
                    newProcess.burstTime,
                    newProcess.arrivalTime,
                    newProcess.id,
                    newProcess,
                ),
            )

    def onProcessorTimeIncrease(self, processorTime: int):
        self.passIdleTime(processorTime - 1)
        self.enqueueProcesses(processorTime)

    def hasProcessesLeft(self):
        return len(self.processes) > 0

    def hasProcessessInQueue(self):
        return len(self.q) > 0

    def tryDispatchProcess(self, processorTime: int):
        if not self.hasProcessessInQueue() or self.q[0][3].arrivalTime > processorTime:
            return None
        _, _, _, process = heapq.heappop(self.q)
        process.timeOfDispatch = processorTime
        processDispatch = ProcessDispatch(process, self.timeQuantum)
        return processDispatch

    def requeueProcess(self, process: Process, processorTime: int):
        heapq.heappush(
            self.q, (process.timeRemaining, processorTime, process.id, process)
        )

    def passIdleTime(self, processorTime: int):
        for process in self.q:
            processId = process[2]
            self.visualizer.trackProcessAction(processId, processorTime, "W")
            process[3].idleTime += 1

    def initTimeQuantum(self):
        self.timeQuantum = initTimeQuantum()


class RRScheduler(Scheduler):
    def __init__(self, numberOfProcesses: int, visualizer: Visualizer):
        self.numberOfProcesses = numberOfProcesses
        self.processes = []
        self.q = deque([])
        self.timeQuantum = 1
        self.visualizer = visualizer

    def getProcesses(self):
        displayProcessPropertyInfo()

        for i in range(self.numberOfProcesses):
            self.processes.append(initProcess(i + 1))
        self.processes.sort(key=lambda p: p.arrivalTime)
        self.processes = deque(self.processes)

    def enqueueProcesses(self, processorTime: int):
        while (
            self.hasProcessesLeft() and self.processes[0].arrivalTime <= processorTime
        ):
            newProcess = self.processes.popleft()
            self.q.append(newProcess)

    def onProcessorTimeIncrease(self, processorTime: int):
        self.passIdleTime(processorTime - 1)
        self.enqueueProcesses(processorTime)

    def hasProcessesLeft(self):
        return len(self.processes) > 0

    def hasProcessessInQueue(self):
        return len(self.q) > 0

    def tryDispatchProcess(self, processorTime: int):
        if not self.hasProcessessInQueue() or self.q[0].arrivalTime > processorTime:
            return None
        process = self.q.popleft()
        process.timeOfDispatch = processorTime
        processDispatch = ProcessDispatch(process, self.timeQuantum)
        return processDispatch

    def requeueProcess(self, process: Process, processorTime: int):
        self.q.append(process)

    def passIdleTime(self, processorTime: int):
        for process in self.q:
            processId = process.id
            self.visualizer.trackProcessAction(processId, processorTime, "W")
            process.idleTime += 1

    def initTimeQuantum(self):
        self.timeQuantum = initTimeQuantum()


class PScheduler(Scheduler):
    def __init__(self, numberOfProcesses: int, visualizer: Visualizer):
        self.numberOfProcesses = numberOfProcesses
        self.processes = []
        self.q = []
        self.visualizer = visualizer

    def getProcesses(self):
        displayProcessPropertyInfo()

        for i in range(self.numberOfProcesses):
            self.processes.append(initProcess(i + 1, True))
        self.processes.sort(key=lambda p: p.arrivalTime)
        self.processes = deque(self.processes)

    def enqueueProcesses(self, processorTime: int):
        while (
            self.hasProcessesLeft() and self.processes[0].arrivalTime <= processorTime
        ):
            newProcess = self.processes.popleft()
            heapq.heappush(
                self.q,
                (
                    -newProcess.priority,
                    newProcess.arrivalTime,
                    newProcess.id,
                    newProcess,
                ),
            )

    def onProcessorTimeIncrease(self, processorTime: int):
        self.passIdleTime(processorTime - 1)
        self.enqueueProcesses(processorTime)

    def hasProcessesLeft(self):
        return len(self.processes) > 0

    def hasProcessessInQueue(self):
        return len(self.q) > 0

    def tryDispatchProcess(self, processorTime: int):
        if not self.hasProcessessInQueue() or self.q[0][3].arrivalTime > processorTime:
            return None
        _, _, _, process = heapq.heappop(self.q)
        process.timeOfDispatch = processorTime
        processDispatch = ProcessDispatch(process, process.burstTime)
        return processDispatch

    def passIdleTime(self, processorTime):
        for process in self.q:
            processId = process[2]
            self.visualizer.trackProcessAction(processId, processorTime, "W")
            process[3].idleTime += 1


def initTimeQuantum():
    value = int(input(f"Enter the time quantum for the scheduler: "))
    if value <= 0:
        raise Exception("The time quantum must be greater than 0")
    return value


def displayAlgoOptions():
    info = """
    Scheduling Algorithm Options:
    -----------------------------------

    1. First Come First Serve (FCFS)
        - Processes are served in the order
          that they show up to the queue

        | Preemptive | Priority Based | 
        -------------------------------
        |     ❌     |       ❌       |

    2. Shortest Process Next (SPN)
        - Processes are served based on 
        which process has the shortest 
        burst time in the queue

        | Preemptive | Priority Based | 
        -------------------------------
        |     ❌     |       ❌       |

    3. Shortest Remaining Time (SRT)
        - Processes are served based on which
          process has the shortest amount of time left to be executed in the queue
        - Processes will be allotted a certain
          amount of CPU time
        
        | Preemptive | Priority Based | 
        -------------------------------
        |     ✅     |       ❌       |

    4. Round Robin (RR)
        - Processes will be served in a
          circular fashion throughout the queue
        - Processes will be allotted a
          certain amount of CPU time
        - When the allotted time is used
          up, if their is time remaining
          in the process it will be sent
          to the back of the queue

        | Preemptive | Priority Based | 
        -------------------------------
        |     ✅     |       ❌       |

    5. Priority Scheduling (Non-Preemptive)
        - Processes will be served based
          on their priority
        - Processes with the same priority
          will be served on a FCFS basis

        | Preemptive | Priority Based | 
        -------------------------------
        |     ❌     |       ✅       |

    -----------------------------------
"""
    print(info)


def tryGetAlgo():
    value = int(
        input(f"Enter the number associated with the algorithm you would like to run: ")
    )
    if value < 1 or value > 5:
        raise Exception("The value you enter must be within 1 <= val <= 5")
    return value


algoOptions = [FCFSScheduler, SPNScheduler, SRTScheduler, RRScheduler, PScheduler]


def initAlgo():
    displayAlgoOptions()
    value = tryGetAlgo()

    return algoOptions[value - 1]
