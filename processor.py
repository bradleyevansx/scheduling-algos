from algo import ProcessDispatch, Scheduler
from visual import Visualizer


class Processor:
    def __init__(self, scheduler: Scheduler, visualizer: Visualizer):
        self.scheduler = scheduler
        self.processorTime = 0
        self.visualizer = visualizer
    
    def increaseProcessorTime(self):
        self.processorTime += 1
        self.scheduler.onProcessorTimeIncrease(self.processorTime)
    
    def run(self):
        self.scheduler.enqueueProcesses(self.processorTime)
        while self.scheduler.hasProcessesLeft() or self.scheduler.hasProcessessInQueue():
            processDispatch = self.scheduler.tryDispatchProcess(self.processorTime)
            if processDispatch is None:
                self.increaseProcessorTime()
                continue
            self.executeProcessDispatch(processDispatch)
        self.visualizer.visualize(self.processorTime)
    
    def executeProcessDispatch(self, processDispatch: ProcessDispatch):
        while processDispatch.timeQuantum > 0 and processDispatch.process.timeRemaining > 0:
            self.visualizer.trackProcessAction(processDispatch.process.id, self.processorTime, "E")
            processDispatch.timeQuantum -= 1
            processDispatch.process.timeRemaining -= 1
            self.increaseProcessorTime()
        if processDispatch.process.timeRemaining > 0:
            self.scheduler.requeueProcess(processDispatch.process, self.processorTime)

