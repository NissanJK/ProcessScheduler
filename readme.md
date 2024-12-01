### **Process Scheduler Simulator**

#### **Description**
The **Process Scheduler Simulator** is a Python-based project that simulates common CPU scheduling algorithms, including:  
- **First Come First Serve (FCFS)**  
- **Shortest Job First (SJF)**  
- **Round Robin (RR)**  
- **Priority Scheduling**

This project is designed for educational purposes to demonstrate how operating systems manage CPU scheduling among processes. It calculates **waiting times**, **turnaround times**, and visualizes process execution using Gantt charts.

---

### **Features**
- Supports four CPU scheduling algorithms.  
- Interactive user input for processes.  
- Calculates average waiting time and average turnaround time.  
- Displays Gantt charts for better understanding.  

---

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/NissanJK/ProcessScheduler.git
   cd ProcessScheduler
   ```

2. Install Python dependencies:
   ```bash
   pip install matplotlib
   ```

---

### **Usage**
Run the program using the following command:
```bash
python main.py
```

Follow the on-screen prompts to:  
1. Choose a scheduling algorithm.  
2. Enter process details (arrival time, burst time, priority, etc.).  
3. View results and Gantt charts.

---

### **Example**
**Input**:  
- Number of Processes: 3  
- Algorithm: FCFS  
- Processes:  
  - P1: Arrival = 0, Burst = 5  
  - P2: Arrival = 1, Burst = 3  
  - P3: Arrival = 2, Burst = 8  

**Output**:  
```
Process Arrival Burst Waiting Turnaround
P1      0       5     0        5
P2      1       3     4        7
P3      2       8     6        14

Average Waiting Time: 3.33
Average Turnaround Time: 8.67
```

A Gantt chart will also be displayed.

### **Project Report**
[ProcessScheduler](/ProcessScheduler.pdf)