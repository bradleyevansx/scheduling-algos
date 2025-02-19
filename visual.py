class Visualizer:
    def initProcesses(self, processCount: int):
        self.processes = {id: [] for id in range(1, processCount + 1)} 

    def trackProcessAction(self, processId:int, processorTime: int, action: str):
        self.processes[processId].append((processorTime, action))

    def getWaitTimes(self):
        waitTimes = []

        for key in self.processes:
            curr = 0
            for _, action in self.processes[key]:
                if action == "W":
                    curr += 1
            waitTimes.append(curr)
        return waitTimes
    def getTurnAroundTimes(self):
        turnTimes = []

        for key in self.processes:
            actions = self.processes[key]
            first, last = actions[0][0], actions[-1][0]
            turnTimes.append(last - first + 1)
        return turnTimes
    def getResponseTimes(self):
        resTimes = []

        for key in self.processes:
            actions = self.processes[key]
            arrivalTime = actions[0][0]
            for pTime, action in actions:
                if action == "E":
                    resTimes.append(pTime - arrivalTime)
                    break
        return resTimes
    
    def visualize(self, totalProcessorTime: int):
        visual = [[" " for _ in range(len(self.processes) + 1)] for _ in range(totalProcessorTime + 1)]
        
        for processId in self.processes:
            actions = self.processes[processId]
            for pTime, action in actions:
                visual[pTime][processId] = action

        header = "| Time |" + "|".join(f" P {i} " for i in range(1, len(self.processes) + 1)) + "|"
        
        print(header)

        for time, row in enumerate(visual):
            formattedRow = f"| {time:04} | " + " | ".join([f" {action} " for action in row[1:]]) + " |"
            print(formattedRow)
        
        n = len(header)
        text = "Times for each process"
        textN = len(text)

        sidesN = (n - textN) // 2
        side = " ".join(["" for _ in range(sidesN)])
        
        if n > 25:
            print("|" + side + text + side + "|")
        waitTimes = self.getWaitTimes()
        turnTimes = self.getTurnAroundTimes()
        resTimes = self.getResponseTimes()
        print("| Wait | " + " | ".join([f"{time:03}" for time in waitTimes]) + " |")
        print("| Turn | " + " | ".join([f"{time:03}" for time in turnTimes]) + " |")
        print("| Resp | " + " | ".join([f"{time:03}" for time in resTimes]) + " |")
        pCount = len(waitTimes)
        averageWait = sum(waitTimes) // pCount
        averageTurn = sum(turnTimes) // pCount
        averageRes = sum(resTimes) // pCount
        print("|  Averages  |")
        print(f"| Wait | {averageWait:03} |")
        print(f"| Turn | {averageTurn:03} |")
        print(f"| Resp | {averageRes:03} |")