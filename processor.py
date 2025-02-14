from algo import ProcessDispatch, Scheduler


class Processor:
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler
        self.processorTime = 0
    
    def increaseProcessorTime(self):
        self.processorTime += 1
        self.scheduler.onProcessorTimeIncrease(self.processorTime)
    
    def run(self):
        while self.scheduler.hasProcessesLeft() or self.scheduler.hasProcessessInQueue():
            print("processor time: ", self.processorTime)
            processDispatch = self.scheduler.tryDispatchProcess(self.processorTime)
            if processDispatch is None:
                print("no process to execute")
                self.increaseProcessorTime()
                continue
            self.executeProcessDispatch(processDispatch)
    
    def executeProcessDispatch(self, processDispatch: ProcessDispatch):
        print("executing process: ", processDispatch.process.id, processDispatch.timeQuantum)
        while processDispatch.timeQuantum > 0:
            processDispatch.timeQuantum -= 1
            processDispatch.process.timeRemaining -= 1
            self.increaseProcessorTime()

