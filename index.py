from algo import initAlgo
from processor import Processor
from visual import Visualizer

def main():
    numberOfProcesses = int(input("Enter the number of processes: "))
    if numberOfProcesses <= 0:
        print("Number of processes must be greater than 0")
        return
    
    visualizer = Visualizer()

    visualizer.initProcesses(numberOfProcesses) 

    schedulerAlgo = initAlgo()

    scheduler = schedulerAlgo(numberOfProcesses, visualizer)

    if hasattr(schedulerAlgo, 'initTimeQuantum'):
        scheduler.initTimeQuantum()

    scheduler.getProcesses()


    

    processor = Processor(scheduler, visualizer)

    processor.run()

    
    
    
main()