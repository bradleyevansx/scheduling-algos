# Scheduling Algorithms

## About this Repository

This repository contains the code for a school project in my **Operating Systems** class.

There are a couple important classes that make this program work.

### User Input

Firstly there is the way I allowed the user input.

- I wouldn't do it this way again
- I have a base class called ProcessProperty which I implement with all the properties.
- I did this before I realized how little there was to take in per process and wanted to mess around with inheritance and abstract classes in python because I have not done it before.

Second there is the process class itself.

- This class holds important information like arrival time, burst time, and priority.
- In addition to these values the value of time remaining and idle time are updated by the processor and the scheduler throughout the program.
- The idle time is a bit of a waste of space. It could be used for some features I had thought of as I was creating the program but ultimately it is not needed.

Third there is the scheduler.

- This implements the scheduling algorithms we are looking to analyze.
- The five types are FCFC, SPN, SRT, RR and P.
- They are all very similar which is why I chose to give them a parent abstract class which is essentially an interface since I did not implement any funcions.

Fourth there is the processor.

- The processor takes in a scheduler and also functions as the system clock of some sort.
- On increase of the processor time the scheduler is notified so that it can increase the idle time of waiting processes and enqueue any processes that have arrived.

Lastly there is the visualizer.

- This object will belong to the scheduler and processor.
- On idle time increase and execution of the active process the state of each process in the visualizer is updated.
- This happens throughout the entire time the process is executing so that you can calculate all metrics and display the state of the program throughout execution very easily.

Next steps.

- Algo that times time waiting into consideration to prevent starvation ?
- Algo that mixes priority into the shortest based ones ?
- Replay simulation with same processes but different algo ?
- Generate random process states ?
- Take input from http request and stream response back to front end ?
- Testing ?

## About the Project

The requirements for the project are as follows:

**Objectives:**

- To simulate and visualize various CPU scheduling algorithms.
- To compare the performance of different algorithms based on metrics such as turnaround time, waiting
  time, and response time.

**Scheduling Algorithms to Implement:**

1. First-Come, First-Served (FCFS)
2. Shortest Process Next (SPN)
3. Shortest Remaining Time (SRT)
4. Round Robin (RR)
5. Priority Scheduling (Non-Preemptive)

**Features:**

- User Input: Allow users to input process details (e.g., process ID, arrival time, burst time, priority).
- Algorithm Selection: Let users choose which scheduling algorithm to simulate.
- Visualization: Create a graphical representation of the scheduling process, such as Gantt charts.
- Metrics Calculation: Automatically calculate and display key performance metrics (average waiting time, average turnaround time, and response time).

**Tools and Technologies:**
• Programming Language: `Python`, `Java`, or `C++`

**Implementation Steps:**

1. Input: Use command line arguments or prompt the user for input.
2. Implement the Algorithms: Write functions for each scheduling algorithm.
3. Output: Create a function to draw Gantt charts based on the scheduling order.
4. Calculate Metrics: Implement functions to compute average waiting time, turnaround time, and
   response time.
5. Testing and Validation: Test with various sets of process data to validate accuracy.

**Deliverables:**

- Single compressed file containing your source code and presentation/report.
