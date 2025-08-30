#include <iostream>
#include <vector>
#include <limits.h> // for INT_MAX
using namespace std;

class Process {
public:
    int p_id;   // Process ID
    int at;     // Arrival Time
    int bt;     // Burst Time
    int ct;     // Completion Time
    int tat;    // Turnaround Time
    int wt;     // Waiting Time
    bool done;  // Completed or not

    Process(int id, int arrival, int burst) {
        p_id = id;
        at = arrival;
        bt = burst;
        ct = tat = wt = 0;
        done = false;
    }
};

int main() {
    int n;
    cout << "Enter number of Processes: ";
    cin >> n;

    vector<Process> processes;
    for (int i = 0; i < n; i++) {
        int id, at, bt;
        cout << "\nEnter Process Number: ";
        cin >> id;
        cout << "Enter Arrival Time: ";
        cin >> at;
        cout << "Enter Burst Time: ";
        cin >> bt;
        processes.push_back(Process(id, at, bt));
    }

    int completed = 0, current_time = 0;

    while (completed < n) {
        int idx = -1;
        int min_bt = INT_MAX;

        // Find process with minimum burst time among available
        for (int i = 0; i < n; i++) {
            if (!processes[i].done && processes[i].at <= current_time && processes[i].bt < min_bt) {
                min_bt = processes[i].bt;
                idx = i;
            }
        }

        if (idx == -1) {
            // No process ready, increment time
            current_time++;
        } else {
            // Execute selected process
            Process &p = processes[idx];
            p.ct = current_time + p.bt;
            p.tat = p.ct - p.at;
            p.wt = p.tat - p.bt;
            p.done = true;

            current_time = p.ct;
            completed++;

            cout << "\nProcess ID: " << p.p_id
                 << " | AT: " << p.at
                 << " | BT: " << p.bt
                 << " | CT: " << p.ct
                 << " | TAT: " << p.tat
                 << " | WT: " << p.wt;
        }
    }

    return 0;
}
