from algo import initAlgo
from processor import Processor

def main():
    numberOfProcesses = int(input("Enter the number of processes: "))
    if numberOfProcesses <= 0:
        print("Number of processes must be greater than 0")
        return

    schedulerAlgo = initAlgo()

    scheduler = schedulerAlgo(numberOfProcesses)

    if schedulerAlgo.initTimeQuantum:
        scheduler.initTimeQuantum()

    scheduler.getProcesses()


    

    processor = Processor(scheduler)

    processor.run()

    
    
    
main()