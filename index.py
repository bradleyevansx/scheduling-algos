from algo import initAlgo
from process import displayProcessPropertyInfo, initProcess
from processor import Processor

def main():
    numberOfProcesses = int(input("Enter the nubmer of processes: "))

    processes = []

    displayProcessPropertyInfo()

    for i in range(numberOfProcesses):
        processes.append(initProcess(i + 1))
    
    schedulerAlgo = initAlgo()

    scheduler = schedulerAlgo(processes)

    processor = Processor(scheduler)

    processor.run()

    for process in processes:
        print(process.__dict__)
    
    initAlgo()
    
main()