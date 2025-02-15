from algo import initAlgo
from processor import Processor

def main():
    numberOfProcesses = int(input("Enter the nubmer of processes: "))
    if numberOfProcesses <= 0:
        print("Number of processes must be greater than 0")
        return

    processes = []
    schedulerAlgo = initAlgo()

    scheduler = schedulerAlgo(numberOfProcesses)

    scheduler.getProcesses()

    processor = Processor(scheduler)

    processor.run()

    for process in processes:
        print(process.__dict__)
    
    
main()