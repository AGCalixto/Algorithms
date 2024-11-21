# Round-Robin Algorithm (RR)
# The RR Algorithm is Preemptive by design as it may switch between processes at a defined time.
# The time at which the processes may switch is called quantum time.
# For this time, the quantum time will be 3 milliseconds.

def RR(processes, n, quantum):
    # Initialize time variables and lists to 0 for completion, waiting and turnaround times.
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    # Get the remaining time for all the processes so we can eventually reduce or add time.
    # This time reduction or addition depends on the process' burst time and the quantum time.
    remaining_burst_time = [process[2] for process in processes]

    # Current time in the scheduling process
    time = 0
    # The done variable is set to false, and the program will run till it becomes True.
    done = False

    while not done:
        done = True
        for i in range(n):
            # Check if there is remaining burst time of a previously worked process
            if remaining_burst_time[i] > 0:
                done = False  # At least one process is still running so the program continues.

                if remaining_burst_time[i] > quantum:
                    # Increment the time by quantum if process exceeds quantum.
                    time += quantum
                    # Reduce the remaining burst time for the process by the quantum
                    remaining_burst_time[i] -= quantum
                else:
                    # Process Completion
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - processes[i][2] - processes[i][1]
                    remaining_burst_time[i] = 0
                    completion_time[i] = time
                    turnaround_time[i] = completion_time[i] - processes[i][1]

    return completion_time, turnaround_time, waiting_time

# Function to calculate average turnaround and waiting times
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
# The Processes have 3 categories.
# 1. Name, 2. Arrival Time, 3. Burst Time
processes = [
    ["P1", 0, 3], ["P2", 2, 4], ["P3", 3, 1], ['P4', 4, 3], ["P5", 5, 4],
    ["P6", 23, 15], ["P7", 5, 8], ["P8", 5, 12], ['P9', 15, 1], ["P10", 10, 2],
    ["P11", 1, 4], ["P12", 0, 7], ["P13", 3, 4], ['P14', 1, 6], ["P15", 8, 3],
    ["P16", 6, 8], ["P17", 6, 3], ["P18", 12, 13], ['P19', 7, 4], ["P20", 5, 10]
]

n = len(processes)
quantum = 3 # milliseconds for realistic time.

completion_time, turnaround_time, waiting_time = RR(processes, n, quantum)

print('The Round Robin Algorithm')
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
