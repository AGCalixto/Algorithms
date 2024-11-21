# Shortest Job First Algorithm (Preemptive / Shortest Remaining Time First)

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

def SJF_Preemptive(processes, n):
    # Sort the processes by arrival time initially
    processes.sort(key=lambda x: x[1])

    # Initialize variables
    remaining_time = [p[2] for p in processes]  # Track remaining burst time for each process
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    current_time = 0
    completed = 0
    shortest = None  # Index of the process with the shortest remaining time

    while completed < n:
        # Find process with the shortest remaining time that's arrived and not completed
        shortest = None
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0:
                if shortest is None or remaining_time[i] < remaining_time[shortest]:
                    shortest = i

        if shortest is not None:
            # Process the selected shortest job
            remaining_time[shortest] -= 1
            current_time += 1

            # Check if the process is completed
            if remaining_time[shortest] == 0:
                completed += 1
                completion_time[shortest] = current_time
                turnaround_time[shortest] = completion_time[shortest] - processes[shortest][1]
                waiting_time[shortest] = turnaround_time[shortest] - processes[shortest][2]
        else:
            # If no process is available, increment time
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

# Run SJF Preemptive algorithm
completion_time, turnaround_time, waiting_time = SJF_Preemptive(processes, n)

# Display results
print('Shortest Job First (Preemptive / Shortest Remaining Time First) Algorithm')
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
