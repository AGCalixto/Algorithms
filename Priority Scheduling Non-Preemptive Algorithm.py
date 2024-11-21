# Priority Scheduling (Non-Preemptive) Algorithm

# This type of Algorithm, follows the basic FCFS Algorithm rules, but a new rule is added to the game.
# This new rule refers to the priority of each process.
# The priority of each process defines which process will start first.
# In this case, the process with the most priority will be the one with the lowest number.
# Ex. Processes with priority 1, will be executed first than processes with priority 2.


def PriorityScheduling(processes, n):
    # Sort processes by priority, breaking ties by arrival time
    processes.sort(key=lambda x: (x[3], x[1]))  # Priority first, then Arrival Time

    # ------------------C-O-M-P-L-E-T-I-O-N--T-I-M-E-----------------------------------
    # The completion time is just the total time it takes for a task to be finished
    # Create a list of 0s for the completion times
    completion_time = [0] * n
    current_time = 0

    for index in range(n):
        arrival_time = processes[index][1]
        burst_time = processes[index][2]

        # Update current time based on arrival time if there is idle time
        if current_time < arrival_time:
            current_time = arrival_time

        current_time += burst_time
        completion_time[index] = current_time

    # ----------------T-U-R-N-A-R-O-U-N-D--T-I-M-E--------------------------------
    # The Turnaround Time is the difference between the Total current time and completion time.
    # Create list for initiation.
    turnaround_time = [0] * n
    # Turn around Time = Total time - Arrival time
    for index in range(n):
        turnaround_time[index] = completion_time[index] - processes[index][1]

    # ------------------W-A-I-T-I-N-G--T-I-M-E-----------------------------------
    # The Waiting Time is the difference between the Turnaround Time and the Burst Time.
    # Create a list with all the waiting times for the processes starting at 0.
    # Waiting Time = TurnAround Time - Burst Time
    waiting_time = [0] * n
    for index in range(n):
        waiting_time[index] = turnaround_time[index] - processes[index][2]

    return completion_time, turnaround_time, waiting_time

# ------------------A-V-E-R-A-G-E--T-U-R-N-A-R-O-U-N-D--T-I-M-E--------------------
# You can obtain the Average Turnaround Time by adding all the turnaround times.
# Then divide them by the number of processes.
def AVG_TAT(turnaround_time, n):
    avg_tat = 0
    for index in range(0, n):
        avg_tat += turnaround_time[index]
    avg_tat = avg_tat/n
    return avg_tat

# ------------------A-V-E-R-A-G-E--W-A-I-T-I-N-G--T-I-M-E--------------------------
# The Average Waiting Time is achievable by adding all the waiting times.
# Then divide the result by the number of processes.
def AVG_WT(waiting_time, n):
    avg_wt = 0
    for index in range(0,n):
        avg_wt += waiting_time[index]
    avg_wt = avg_wt/n
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
completion_time, turnaround_time, waiting_time = PriorityScheduling(processes, n)

print('The Priority Scheduling Algorithm')
print('---------------------------------------------------------')
print('NOTE: The printing process is not organized in this algorithm')
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