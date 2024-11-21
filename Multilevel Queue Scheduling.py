# Multilevel Queue Scheduling Algorithm

#

def FCFS(processes, n):
    # ------------------C-O-M-P-L-E-T-I-O-N--T-I-M-E-----------------------------------
    # The completion time is just the total time it takes for a task to be finished
    # Create a list of 0s for the completion times
    completion_time = [0] * n
    current_time = 0

    for index in range(n):
        # Obtain the arrival and burst time from each process
        arrival_time = processes[index][1]
        burst_time = processes[index][2]

        # Update current time based on arrival time if there's idle time
        if current_time < arrival_time:
            current_time = arrival_time

        # Process execution and completion time calculation
        current_time += burst_time
        completion_time[index] = current_time

    # ----------------T-U-R-N-A-R-O-U-N-D--T-I-M-E--------------------------------
    # The Turnaround Time is the difference between the Total current time and completion time.
    # Create list for initiation.
    # Turn around Time = Total time - Arrival time

    turnaround_time = [completion_time[i] - processes[i][1] for i in range(n)]

    # ------------------W-A-I-T-I-N-G--T-I-M-E-----------------------------------
    # The Waiting Time is the difference between the Turnaround Time and the Burst Time.
    # Create a list with all the waiting times for the processes starting at 0.
    # Waiting Time = TurnAround Time - Burst Time

    waiting_time = [turnaround_time[i] - processes[i][2] for i in range(n)]

    return completion_time, turnaround_time, waiting_time

## ------------------A-V-E-R-A-G-E--T-U-R-N-A-R-O-U-N-D--T-I-M-E--------------------
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

# Multilevel Queue Scheduling function
def MultilevelQueueScheduling(processes, n):
    # Divide processes into two queues based on their priority level
    queue1 = [p for p in processes if p[3] == "High"]
    queue2 = [p for p in processes if p[3] == "Low"]

    print("Processing Queue 1 (High Priority):")
    completion_time1, turnaround_time1, waiting_time1 = FCFS(queue1, len(queue1))
    print("Processing Queue 2 (Low Priority):")
    completion_time2, turnaround_time2, waiting_time2 = FCFS(queue2, len(queue2))

    # Combine results for each queue to get overall results
    completion_time = completion_time1 + completion_time2
    turnaround_time = turnaround_time1 + turnaround_time2
    waiting_time = waiting_time1 + waiting_time2

    return completion_time, turnaround_time, waiting_time

# List for the processes.
# The Processes have 4 categories.
# 1. Name, 2. Arrival Time, 3. Burst Time, 4. Priority (Can be 'High' or 'Low')
processes = [
    ["P1", 0, 3, "High"], ["P2", 2, 4, "Low"], ["P3", 3, 1, "High"], ["P4", 4, 3, "Low"], ["P5", 5, 4, "High"],
    ["P6", 23, 15, "Low"], ["P7", 5, 8, "High"], ["P8", 5, 12, "Low"], ["P9", 15, 1, "High"], ["P10", 10, 2, "Low"],
    ["P11", 1, 4, "High"], ["P12", 0, 7, "Low"], ["P13", 3, 4, "High"], ["P14", 1, 6, "Low"], ["P15", 8, 3, "High"],
    ["P16", 6, 8, "Low"], ["P17", 6, 3, "High"], ["P18", 12, 13, "Low"], ["P19", 7, 4, "High"], ["P20", 5, 10, "Low"]
]

n = len(processes)
completion_time, turnaround_time, waiting_time = MultilevelQueueScheduling(processes, n)

print('Multilevel Queue Scheduling Algorithm')
print('---------------------------------------------------------')
for index, (name, arrival_time, burst_time, priority) in enumerate(processes):
    print(
        f'Name: {name}, Arrival Time: {arrival_time}, Burst Time: {burst_time}, Priority: {priority}, '
        f'Completion Time: {completion_time[index]}, Turnaround Time: {turnaround_time[index]} milliseconds, '
        f'Waiting Time: {waiting_time[index]} milliseconds')
print('---------------------------------------------------------')
print(f'The Average Waiting Time is: {AVG_WT(waiting_time, n):.2f} milliseconds')
print(f'The Average Turnaround Time is: {AVG_TAT(turnaround_time, n):.2f} milliseconds')
print(f'CPU Utilization: {CPU_Utililzation(processes, n, completion_time):.2f}%')
print(f'Throughput: {Throughput(n, completion_time):.2f} processes per unit time')
