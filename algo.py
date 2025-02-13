from typing import List
from process import Process

class FCFSScheduler:
    def __init__(self, processes: List[Process]):
        self.processes = processes

    def prioritizeProcesses(self):
        self.processes.sort(key=lambda process: process.arrivalTime)


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
    displayAlogOptions()
    value = tryGetAlgo()
    print(value)