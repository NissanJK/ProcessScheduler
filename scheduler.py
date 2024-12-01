from utils import print_results, plot_gantt_chart

class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def fcfs(self):
        self.processes.sort(key=lambda x: x[1])  # Sort by arrival time
        current_time = 0
        waiting_time = []
        turnaround_time = []
        gantt_chart = []

        for pid, arrival, burst, _ in self.processes:
            if current_time < arrival:
                current_time = arrival
            waiting_time.append(current_time - arrival)
            gantt_chart.append((pid, current_time, current_time + burst))
            current_time += burst
            turnaround_time.append(current_time - arrival)

        print_results(self.processes, waiting_time, turnaround_time)
        plot_gantt_chart(gantt_chart, "FCFS")

    def sjf(self):
        self.processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
        current_time = 0
        waiting_time = []
        turnaround_time = []
        gantt_chart = []
        ready_queue = []
        remaining_processes = list(self.processes)

        while remaining_processes or ready_queue:
            ready_queue.extend([p for p in remaining_processes if p[1] <= current_time])
            remaining_processes = [p for p in remaining_processes if p not in ready_queue]
            if ready_queue:
                ready_queue.sort(key=lambda x: x[2])  # Sort by burst time
                pid, arrival, burst, _ = ready_queue.pop(0)
                waiting_time.append(current_time - arrival)
                gantt_chart.append((pid, current_time, current_time + burst))
                current_time += burst
                turnaround_time.append(current_time - arrival)
            else:
                current_time += 1

        print_results(self.processes, waiting_time, turnaround_time)
        plot_gantt_chart(gantt_chart, "SJF")

    def round_robin(self, quantum):
        current_time = 0
        queue = self.processes[:]
        waiting_time = [0] * len(self.processes)
        turnaround_time = [0] * len(self.processes)
        remaining_burst = {p[0]: p[2] for p in self.processes}
        gantt_chart = []

        while queue:
            pid, arrival, burst, _ = queue.pop(0)
            if current_time < arrival:
                current_time = arrival
            execution_time = min(quantum, remaining_burst[pid])
            gantt_chart.append((pid, current_time, current_time + execution_time))
            current_time += execution_time
            remaining_burst[pid] -= execution_time
            if remaining_burst[pid] > 0:
                queue.append((pid, arrival, burst, 0))
            else:
                turnaround_time[pid - 1] = current_time - arrival
                waiting_time[pid - 1] = turnaround_time[pid - 1] - burst

        print_results(self.processes, waiting_time, turnaround_time)
        plot_gantt_chart(gantt_chart, "Round Robin")

    def priority_scheduling(self):
        self.processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time, then priority
        current_time = 0
        waiting_time = []
        turnaround_time = []
        gantt_chart = []

        for pid, arrival, burst, priority in self.processes:
            if current_time < arrival:
                current_time = arrival
            waiting_time.append(current_time - arrival)
            gantt_chart.append((pid, current_time, current_time + burst))
            current_time += burst
            turnaround_time.append(current_time - arrival)

        print_results(self.processes, waiting_time, turnaround_time)
        plot_gantt_chart(gantt_chart, "Priority Scheduling")
