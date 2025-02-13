from algo import initAlgo
from process import displayProcessPropertyInfo, initProcess

def main():
    numberOfProcesses = int(input("Enter the nubmer of processes: "))

    processes = []

    displayProcessPropertyInfo()

    for i in range(numberOfProcesses):
        processes.append(initProcess(i + 1))
    
    initAlgo()
    








main()