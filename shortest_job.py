# Define a Process class to hold process info
class Process:
    def __init__(self, p_id, at, bt):
        self.p_id = p_id
        self.at = at        # Arrival Time
        self.bt = bt        # Burst Time
        self.ct = 0         # Completion Time
        self.tat = 0        # Turnaround Time
        self.wt = 0         # Waiting Time
        self.done = False   # Flag to mark if process completed

def main():
    n = int(input("Enter number of Processes: "))
    processes = []

    # Input process data
    for _ in range(n):
        p_id = int(input("Enter Process Number: "))
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append(Process(p_id, at, bt))

    completed = 0
    current_time = 0

    while completed < n:
        # Find process with shortest burst time among arrived and not done
        idx = -1
        min_bt = float('inf')

        for i, p in enumerate(processes):
            if (not p.done) and (p.at <= current_time) and (p.bt < min_bt):
                min_bt = p.bt
                idx = i

        if idx == -1:
            # No process ready, increment current time
            current_time += 1
        else:
            # Run the selected process
            p = processes[idx]
            p.ct = current_time + p.bt
            p.tat = p.ct - p.at
            p.wt = p.tat - p.bt
            p.done = True

            current_time = p.ct
            completed += 1

            print(f"Process id {p.p_id}, at {p.at}, bt {p.bt}, ct {p.ct}, tat {p.tat}, wt {p.wt}")

if __name__ == "__main__":
    main()
