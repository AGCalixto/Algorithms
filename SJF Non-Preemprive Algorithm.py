# Shortest Job First Algorithm (Non-Preemptive)

# In this algorithm, processes will have 3 categories.
# 1. Name, 2. Arrival Time, 3. Burst Time

# Formulas and Definitions
# ------------------C-O-M-P-L-E-T-I-O-N--T-I-M-E-----------------------------------
# The completion time is just the total time it takes for a task to be finished

# ----------------T-U-R-N-A-R-O-U-N-D--T-I-M-E--------------------------------
# The Turnaround Time is the difference between the Total current time and completion time.
# Turnaround Time = Total Current Time - Arrival Time

# ------------------W-A-I-T-I-N-G--T-I-M-E-----------------------------------
# The Waiting Time is the difference between the Turnaround Time and the Burst Time.
# Create a list with all the waiting times for the processes starting at 0.
# Waiting Time = TurnAround Time - Burst Time

def SJF(processes, n):
    # Sort the processes by arrival time, then by burst time
    processes.sort(key=lambda x: (x[1], x[2]))

    # Initialize variables of the completion time, turnaround time, waiting time and current time to 0.
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    current_time = 0
    # Track if each process has completed
    is_completed = [False] * n

    for _ in range(n):
        # Find all processes that have arrived and are not completed
        available_processes = [
            (index, j) for index, j in enumerate(processes)
            if j[1] <= current_time and not is_completed[index]
        ]

        if available_processes:
            # Choose the process with the smallest burst time
            available_processes.sort(key=lambda x: x[1][2])
            index, current_process = available_processes[0]

            # Update times
            completion_time[index] = current_time + current_process[2]
            turnaround_time[index] = completion_time[index] - current_process[1]
            waiting_time[index] = turnaround_time[index] - current_process[2]

            # Mark as completed and update the current time
            is_completed[index] = True
            current_time = completion_time[index]
        else:
            # If no process has arrived, move the current time forward
            current_time += 1

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

    return (Total_burst_time / Total_time) * 100


# ------------------T-H-R-O-U-G-H-P-U-T-----------------------------
# The Throughput is the number of processes completed in a given time period.
# It can be calculated by dividing the total number of processes by the time
# when the last process finishes.
# Throughput = N. of Processes / Total Time
def Throughput(n, completion_time):
    Total_time = max(completion_time)
    return n / Total_time


# List for the processes
# The Processes have 3 categories.
# 1. Name, 2. Arrival Time, 3. Burst Time
processes = [["P1", 0, 3], ["P2", 2, 4], ["P3", 3, 1], ['P4', 4, 3], ["P5", 5, 4],
             ["P6", 23, 15], ["P7", 5, 8], ["P8", 5, 12], ['P9', 15, 1], ["P10", 10, 2],
             ["P11", 1, 4], ["P12", 0, 7], ["P13", 3, 4], ['P14', 1, 6], ["P15", 8, 3],
             ["P16", 6, 8], ["P17", 6, 3], ["P18", 12, 13], ['P19', 7, 4], ["P20", 5, 10]]

n = len(processes)
completion_time, turnaround_time, waiting_time = SJF(processes, n)

print('Shortest Job First (Non-Preemptive) Algorithm')
print('---------------------------------------------------------')
print('NOTE: The printing process is not organized in this algorithm')
print('---------------------------------------------------------')
for index, (name, arrival_time, burst_time) in enumerate(processes):
    print(
        f'Name: {name}, Arrival Time: {arrival_time}, Burst Time: {burst_time}, Completion Time: {completion_time[index]}, '
        f'Turnaround Time: {turnaround_time[index]} milliseconds, Waiting Time: {waiting_time[index]} milliseconds')
print('---------------------------------------------------------')
print(f'The Average Waiting Time is: {AVG_WT(waiting_time, n):.2f} milliseconds')
print(f'The Average Turnaround Time is: {AVG_TAT(turnaround_time, n):.2f} milliseconds')
print(f'The CPU Utilization is: {CPU_Utililzation(processes, n, completion_time):.2f}%')
print(f'The Throughput is: {Throughput(n, completion_time):.2f} processes per millisecond')
