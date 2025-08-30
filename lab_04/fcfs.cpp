#include <iostream>
#include <vector>
#include <algorithm> // for sort
using namespace std;

class Process 
{
public:
    int p_id;   // Process ID
    int at;     // Arrival Time
    int bt;     // Burst Time
    int ct;     // Completion Time
    int tat;    // Turnaround Time
    int wt;     // Waiting Time

    Process(int id, int arrival, int burst) 
    {
        p_id = id;
        at = arrival;
        bt = burst;
        ct = tat = wt = 0;
    }
};

int main() 
{
    int n;
    cout << "Enter number of Processes: ";
    cin >> n;

    vector<Process> processes;
    for (int i = 0; i < n; i++) 
    {
        int id, at, bt;
        cout << "\nEnter Process Number: ";
        cin >> id;
        cout << "Enter Arrival Time: ";
        cin >> at;
        cout << "Enter Burst Time: ";
        cin >> bt;
        processes.push_back(Process(id, at, bt));
    }

    // Sort processes by Arrival Time
    sort(processes.begin(), processes.end(),
         [](Process &a, Process &b) { return a.at < b.at; });

    int current_time = 0;
    for (int i = 0; i < n; i++) 
    {
        if (i == 0) 
        {
            processes[i].ct = processes[i].at + processes[i].bt;
        } 
        else 
        {
            if (processes[i].at > current_time)
                processes[i].ct = processes[i].at + processes[i].bt;
            else
                processes[i].ct = processes[i - 1].ct + processes[i].bt;
        }

        current_time = processes[i].ct;

        processes[i].tat = processes[i].ct - processes[i].at;
        processes[i].wt = processes[i].tat - processes[i].bt;
    }

    // Print results
    cout << "\nProcess ID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time\n";
    for (auto &p : processes) {
        cout << "    " << p.p_id
             << "      |      " << p.at
             << "       |     " << p.bt
             << "      |       " << p.ct
             << "         |       " << p.tat
             << "        |      " << p.wt << "\n";
    }

    return 0;
}
