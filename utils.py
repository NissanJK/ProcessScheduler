import matplotlib.pyplot as plt

def print_results(processes, waiting_time, turnaround_time):
    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    for i, process in enumerate(processes):
        print(f"P{process[0]}\t{process[1]}\t{process[2]}\t{waiting_time[i]}\t{turnaround_time[i]}")
    print(f"\nAverage Waiting Time: {sum(waiting_time) / len(waiting_time):.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time) / len(turnaround_time):.2f}")

def plot_gantt_chart(gantt_chart, title):
    fig, ax = plt.subplots()
    for pid, start, end in gantt_chart:
        ax.broken_barh([(start, end - start)], (10 * pid, 9), facecolors=('tab:blue'))
    ax.set_xlabel('Time')
    ax.set_yticks([10 * pid + 5 for pid, _, _ in gantt_chart])
    ax.set_yticklabels([f"P{pid}" for pid, _, _ in gantt_chart])
    ax.set_title(f"Gantt Chart: {title}")
    plt.show()
