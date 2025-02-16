class Visualizer:
    def initProcesses(self, processCount: int):
        self.processes = {id: [] for id in range(1, processCount + 1)} 
        print(self.processes)

    def trackProcessAction(self, processId:int, processorTime: int, action: str):
        print("processId: ", processId, "processorTime: ", processorTime, "action: ", action)
        self.processes[processId].append((processorTime, action))
    
    def visualize(self, totalProcessorTime: int):
        visual = []
        for processId in self.processes:
            actions = self.processes[processId]

            curr = [" " for _ in range(totalProcessorTime + 1)]
            for pTime, action in actions:
                curr[pTime] = action
            visual.append(curr)
        for i, process in enumerate(visual):
            print(i)