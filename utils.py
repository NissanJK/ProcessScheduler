def print_results(processes, waiting_time, turnaround_time):
    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    for i, process in enumerate(processes):
        print(f"P{process[0]}\t{process[1]}\t{process[2]}\t{waiting_time[i]}\t{turnaround_time[i]}")
    print(f"\nAverage Waiting Time: {sum(waiting_time) / len(waiting_time):.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time) / len(turnaround_time):.2f}")

