# FCFS Scheduling in Python

class Process:
    def __init__(self, p_id, at, bt):
        self.p_id = p_id    # Process ID
        self.at = at        # Arrival Time
        self.bt = bt        # Burst Time
        self.ct = 0         # Completion Time (to be calculated)
        self.tat = 0        # Turnaround Time (to be calculated)
        self.wt = 0         # Waiting Time (to be calculated)

def main():
    n = int(input("Enter number of Processes: "))
    processes = []

    # Input process details
    for _ in range(n):
        p_id = int(input("Enter Process Number: "))
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append(Process(p_id, at, bt))

    # Sort processes based on arrival time
    processes.sort(key=lambda x: x.at)

    current_time = 0
    for i, process in enumerate(processes):
        # Calculate completion time
        if i == 0:
            process.ct = process.at + process.bt
        else:
            if process.at > current_time:
                process.ct = process.at + process.bt
            else:
                process.ct = processes[i-1].ct + process.bt

        current_time = process.ct

        # Calculate turnaround time and waiting time
        process.tat = process.ct - process.at
        process.wt = process.tat - process.bt

    # Print results
    print("\nProcess ID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time")
    for p in processes:
        print(f"{p.p_id:^10} | {p.at:^12} | {p.bt:^10} | {p.ct:^15} | {p.tat:^15} | {p.wt:^12}")

if __name__ == "__main__":
    main()