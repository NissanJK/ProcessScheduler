from scheduler import Scheduler

def main():
    print("Welcome to the Process Scheduler Simulator!")
    print("Choose a scheduling algorithm:")
    print("1. First Come First Serve (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin (RR)")
    print("4. Priority Scheduling")
    
    choice = int(input("Enter your choice (1-4): "))
    
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        pid = i + 1
        arrival = int(input(f"Enter arrival time for Process {pid}: "))
        burst = int(input(f"Enter burst time for Process {pid}: "))
        priority = int(input(f"Enter priority for Process {pid} (lower value = higher priority): ")) if choice == 4 else 0
        processes.append((pid, arrival, burst, priority))

    quantum = int(input("Enter time quantum (for RR only): ")) if choice == 3 else None
    
    scheduler = Scheduler(processes)
    
    if choice == 1:
        scheduler.fcfs()
    elif choice == 2:
        scheduler.sjf()
    elif choice == 3:
        scheduler.round_robin(quantum)
    elif choice == 4:
        scheduler.priority_scheduling()
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
