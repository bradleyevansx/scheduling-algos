class Visualizer:
    def initProcesses(self, processCount: int):
        self.processes = {id: [] for id in range(1, processCount + 1)} 

    def trackProcessAction(self, processId:int, processorTime: int, action: str):
        self.processes[processId].append((processorTime, action))
    
    def visualize(self, totalProcessorTime: int):
        visual = []
        print("| Process | " + " | ".join(f"{i:03}" for i in range(totalProcessorTime)) + " |")
        for processId in self.processes:
            actions = self.processes[processId]

            curr = [" " for _ in range(totalProcessorTime + 1)]
            for pTime, action in actions:
                curr[pTime] = action
            visual.append(curr)
        for i, process in enumerate(visual):
            print(f"|   {i+1:03}   | " + " | ".join([f" {action} " for action in process]))