import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scheduler import Scheduler


class ProcessSchedulerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Process Scheduler Simulator")
        self.root.geometry("800x600")
        self.algorithm = tk.StringVar(value="FCFS")
        self.process_data = []
        self.quantum = tk.StringVar()

        self.create_widgets()
        self.figure = None

    def create_widgets(self):
        tk.Label(self.root, text="Select Scheduling Algorithm:").pack(pady=5)
        algorithms = ["FCFS", "SJF", "Round Robin", "Priority Scheduling"]
        for algo in algorithms:
            tk.Radiobutton(self.root, text=algo, variable=self.algorithm, value=algo).pack(anchor="w")

        tk.Label(self.root, text="Add Process (Arrival, Burst, Priority):").pack(pady=5)
        self.process_frame = tk.Frame(self.root)
        self.process_frame.pack()

        self.arrival_entry = self.create_entry("Arrival Time")
        self.burst_entry = self.create_entry("Burst Time")
        self.priority_entry = self.create_entry("Priority (0 if N/A)")

        tk.Button(self.root, text="Add Process", command=self.add_process).pack(pady=5)

        tk.Label(self.root, text="Time Quantum (for RR only):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.quantum).pack()

        tk.Button(self.root, text="Run Scheduler", command=self.run_scheduler).pack(pady=10)

        tk.Label(self.root, text="Process List:").pack(pady=5)
        self.process_list = tk.Text(self.root, height=10, width=50)
        self.process_list.pack()

        self.gantt_frame = tk.Frame(self.root)
        self.gantt_frame.pack(pady=20)

    def create_entry(self, label_text):
        tk.Label(self.process_frame, text=label_text).pack(side="left")
        entry = tk.Entry(self.process_frame)
        entry.pack(side="left")
        return entry

    def add_process(self):
        try:
            arrival = int(self.arrival_entry.get())
            burst = int(self.burst_entry.get())
            priority = int(self.priority_entry.get())

            self.process_data.append((len(self.process_data) + 1, arrival, burst, priority))
            self.update_process_list()

            self.arrival_entry.delete(0, tk.END)
            self.burst_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for Arrival, Burst, and Priority.")

    def update_process_list(self):
        self.process_list.delete(1.0, tk.END)
        for pid, arrival, burst, priority in self.process_data:
            self.process_list.insert(tk.END, f"P{pid}: Arrival={arrival}, Burst={burst}, Priority={priority}\n")

    def run_scheduler(self):
        if not self.process_data:
            messagebox.showerror("Error", "No processes added.")
            return

        algorithm = self.algorithm.get()
        quantum = int(self.quantum.get()) if self.quantum.get().isdigit() else None

        scheduler = Scheduler(self.process_data)
        waiting_time, turnaround_time, gantt_chart = [], [], []

        if algorithm == "FCFS":
            waiting_time, turnaround_time, gantt_chart = scheduler.fcfs()
        elif algorithm == "SJF":
            waiting_time, turnaround_time, gantt_chart = scheduler.sjf()
        elif algorithm == "Round Robin":
            if quantum is None:
                messagebox.showerror("Input Error", "Please enter a valid quantum for Round Robin.")
                return
            waiting_time, turnaround_time, gantt_chart = scheduler.round_robin(quantum)
        elif algorithm == "Priority Scheduling":
            waiting_time, turnaround_time, gantt_chart = scheduler.priority_scheduling()

        avg_waiting_time, avg_turnaround_time = scheduler.calculate_metrics(waiting_time, turnaround_time)
        self.display_gantt_chart(gantt_chart, algorithm)
        messagebox.showinfo("Metrics", f"Average Waiting Time: {avg_waiting_time:.2f}\n"
                                       f"Average Turnaround Time: {avg_turnaround_time:.2f}")

    def display_gantt_chart(self, gantt_chart, title):
        for widget in self.gantt_frame.winfo_children():
            widget.destroy()

        self.figure = Figure(figsize=(6, 3))
        ax = self.figure.add_subplot(111)

        for pid, start, end in gantt_chart:
            ax.broken_barh([(start, end - start)], (10 * pid, 9), facecolors='tab:blue')
        ax.set_xlabel("Time")
        ax.set_yticks([10 * pid + 5 for pid, _, _ in gantt_chart])
        ax.set_yticklabels([f"P{pid}" for pid, _, _ in gantt_chart])
        ax.set_title(f"Gantt Chart: {title}")

        canvas = FigureCanvasTkAgg(self.figure, self.gantt_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def run(self):
        self.root.mainloop()
