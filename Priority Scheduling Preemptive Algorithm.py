# Priority Scheduling (Preemptive) Algorithm

# This type of Algorithm, follows the basic FCFS Algorithm rules, but a new rule is added to the game.
# This new rule refers to the priority of each process.
# The priority of each process defines which process will start first.
# In this case, the process with the most priority will be the one with the lowest number.
# Ex. Processes with priority 1, will be executed first than processes with priority 2.

# As this algorithm is Preemptive, it will have the additional rule that everytime a process is
# being executed, it can be placed aside to give chance to a higher priority process to finish.

def PrioritySchedulingPreemptive(processes, n):
    # Sort processes by arrival time and priority
    processes.sort(key=lambda x: x[1])  # Sort by arrival time to facilitate process arrival tracking

    # Initialize variables through creating lists with 0s on them.
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_burst_time = [process[2] for process in processes]
    current_time = 0
    finished_processes = 0
    last_executed = -1

    while finished_processes < n:
        # Find the process with the highest priority that has arrived
        highest_priority_process = None
        for i in range(n):
            if (processes[i][1] <= current_time and remaining_burst_time[i] > 0 and
                    (highest_priority_process is None or processes[i][3] < processes[highest_priority_process][3])):
                highest_priority_process = i

        # If there's a process to execute, decrement its remaining burst time
        if highest_priority_process is not None:
            if last_executed != highest_priority_process:
                print(f"At time {current_time}, process {processes[highest_priority_process][0]} is executing.")
            remaining_burst_time[highest_priority_process] -= 1
            last_executed = highest_priority_process
            current_time += 1

            # If process is completed
            if remaining_burst_time[highest_priority_process] == 0:
                finished_processes += 1
                completion_time[highest_priority_process] = current_time
                turnaround_time[highest_priority_process] = completion_time[highest_priority_process] - \
                                                            processes[highest_priority_process][1]
                waiting_time[highest_priority_process] = turnaround_time[highest_priority_process] - \
                                                         processes[highest_priority_process][2]
        else:
            current_time += 1  # Idle time if no process is ready

    return completion_time, turnaround_time, waiting_time


# ------------------A-V-E-R-A-G-E--T-U-R-N-A-R-O-U-N-D--T-I-M-E--------------------
# You can obtain the Average Turnaround Time by adding all the turnaround times.
# Then divide them by the number of processes.
def AVG_TAT(turnaround_time, n):
    avg_tat = 0
    for index in range(0, n):
        avg_tat += turnaround_time[index]
    avg_tat = avg_tat / n
    return avg_tat


# ------------------A-V-E-R-A-G-E--W-A-I-T-I-N-G--T-I-M-E--------------------------
# The Average Waiting Time is achievable by adding all the waiting times.
# Then divide the result by the number of processes.
def AVG_WT(waiting_time, n):
    avg_wt = 0
    for index in range(0, n):
        avg_wt += waiting_time[index]
    avg_wt = avg_wt / n
    return avg_wt

# ------------------C-P-U--U-T-I-L-I-Z-A-T-I-O-N--------------------------
# The CPU Utilization is the percentage of time the CPU is actively working (not idle).
# It can be calculated by dividing the total burst time of all the processes by
# the time when the last process finishes.

# CPU Utilization = Total Burst Time / Total Time
def CPU_Utililzation(processes, n, completion_time):
    Total_burst_time = 0
    Total_time = max(completion_time)
    for index in range(1, n):
        Total_burst_time += processes[index][2]

    return (Total_burst_time/Total_time) * 100

# ------------------T-H-R-O-U-G-H-P-U-T-----------------------------
# The Throughput is the number of processes completed in a given time period.
# It can be calculated by dividing the total number of processes by the time
# when the last process finishes.
# Throughput = N. of Processes / Total Time
def Throughput(n, completion_time):
    Total_time = max(completion_time)
    return n/Total_time

# List for the processes.
# The Processes have 4 categories.
# 1. Name, 2. Arrival Time, 3. Burst Time, 4. Priority
processes = [
    ["P1", 0, 3, 2], ["P2", 2, 4, 1], ["P3", 3, 1, 4], ['P4', 4, 3, 3], ["P5", 5, 4, 2],
    ["P6", 23, 15, 1], ["P7", 5, 8, 4], ["P8", 5, 12, 3], ['P9', 15, 1, 2], ["P10", 10, 2, 5],
    ["P11", 1, 4, 2], ["P12", 0, 7, 3], ["P13", 3, 4, 1], ['P14', 1, 6, 4], ["P15", 8, 3, 2],
    ["P16", 6, 8, 3], ["P17", 6, 3, 1], ["P18", 12, 13, 2], ['P19', 7, 4, 4], ["P20", 5, 10, 3]
]

n = len(processes)
completion_time, turnaround_time, waiting_time = PrioritySchedulingPreemptive(processes, n)

print('\nThe Preemptive Priority Scheduling Algorithm')
print('---------------------------------------------------------')
for index, (name, arrival_time, burst_time, priority) in enumerate(processes):
    print(
        f'Name: {name}, Arrival Time: {arrival_time}, Burst Time: {burst_time}, Priority: {priority}, '
        f'Completion Time: {completion_time[index]}, Turnaround Time: {turnaround_time[index]} milliseconds, '
        f'Waiting Time: {waiting_time[index]} milliseconds')
print('---------------------------------------------------------')
print(f'The Average Waiting Time is: {AVG_WT(waiting_time, n):.2f} milliseconds')
print(f'The Average Turnaround Time is: {AVG_TAT(turnaround_time, n):.2f} milliseconds')
print(f'The CPU Utilization is: {CPU_Utililzation(processes, n, completion_time):.2f}%')
print(f'The Throughput is: {Throughput(n, completion_time):.2f} processes per millisecond')