# Process Scheduler Simulator

## Overview
The **Process Scheduler Simulator** is a Python-based application designed to simulate and analyze CPU scheduling algorithms. It features a graphical user interface (GUI) for users to input process details, select scheduling algorithms, and visualize the results with Gantt charts. The simulator calculates key performance metrics such as average waiting time and turnaround time.

## Features
- Supports multiple scheduling algorithms:
  - First Come First Serve (FCFS)
  - Shortest Job First (SJF)
  - Round Robin (RR)
  - Priority Scheduling
- Interactive GUI built with `Tkinter`.
- Displays Gantt charts for visualizing process execution.
- Calculates average waiting time and turnaround time.
- Handles user inputs dynamically.

## Requirements
- Python 3.7 or higher
- Required Libraries:
  - `matplotlib`
  - `tkinter`

To install the dependencies, run:
```bash
pip install matplotlib
```

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/NissanJK/ProcessScheduler.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ProcessScheduler
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Usage
1. Open the application.
2. Select a scheduling algorithm.
3. Add processes by providing the arrival time, burst time, and priority (if applicable).
4. (For Round Robin) Specify the time quantum.
5. Click "Run Scheduler" to execute the algorithm.
6. View results including Gantt charts, average waiting time, and turnaround time.

## Screenshots
### User Interface
![User Interface](screenshot/Screenshot%202024-12-10%20203426.png)
### Simulation Input
![Simulation Input](screenshot/Screenshot%202024-12-10%20203459.png)
### Simulation Results
![Simulation Results](screenshot/Screenshot%202024-12-10%20203309.png)
![Simulation Results](screenshot/Screenshot%202024-12-10%20203251.png)

## Project Structure
```
project/
├── scheduler.py          # Core scheduling algorithms
├── interface.py          # GUI implementation
├── utils.py              # Helper functions (e.g., printing results, Gantt chart plotting)
├── main.py               # Main entry point for the application
├── README.md             # Project documentation
├── ProcessScheduler.pdf  # Project report
```

## Scheduling Algorithms
### 1. First Come First Serve (FCFS)
- Processes are executed in the order of their arrival.
- Non-preemptive scheduling.

### 2. Shortest Job First (SJF)
- Executes the process with the shortest burst time first.
- Non-preemptive scheduling.

### 3. Round Robin (RR)
- Each process gets executed for a fixed quantum time in a cyclic order.
- Preemptive scheduling.

### 4. Priority Scheduling
- Executes processes based on priority (lower values indicate higher priority).
- Non-preemptive scheduling.

## Future Enhancements
- Add support for multilevel queue and feedback queue scheduling.
- Enhance Gantt chart visualization with additional metrics.
- Create web and mobile versions of the application.

### **Project Report**
[ProcessScheduler](/ProcessScheduler.pdf)