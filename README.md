# Scheduling Algorithms

A directory dedicated to show the creation and utilization of diverse scheduling algorithms created with python from scratch.

The algorithms aim to simulate how processes are managed by a CPU, by calculating the Completion Time, Turnaround Time, Waiting Time, CPU Utilization, and Throughput for a given set of processes.

---

## Types of Algorithms

- **First Come First Serve (FCFS)** : The process that requests the CPU first is allocated the CPU first.When the CPU is free, it is allowed to the process at the head of the queue. Is a non-preemptive scheduling algorithm.
- **Shortest Job First (SJF)** : Scheduling policy that selects the waiting process with theh smallest execution time to execute next. Can be preemptive or non-preemptive.
- **Round Robin (RR)** : Scheduling algorithm wherer each process is cyclically assigned a fixed time slot. Preemptive version of FCFS Scheduling algorithm.
- **Priority Scheduling** : Processes are executed based on their priority. The jobs/processes with higher priority are executed first. Priority of processes depends on each circumstance.
- **Multilevel Queue Scheduling** : Applied with the aim of sectioning types of proceesses and then being able to manage them properly. Processes are grouped into several queus using MLQ based on known paramters such as priority, memory, or typpe.

---

## Tech Information

- **Python 3.12**
- `random` - Generates random queues of jobs for the algorithms to complete.
- `time` - used to mimic real-time completion of tasks.

---

## Project Structure

Project/
|-FCFS Algorithm.py
|-Job Generation.py
|-Multilevel Queue Scheduling.py
|-Priority Scheduling Non-Preemptive Algorithm.py
|-Priority Scheduling Preemptive Algorithm.py
|-Round Robin Algorithm.pyp
|-SJF Non-Preemptive Algorithm.py
|-SJF Preemptive Algorithm.py

---

# Architecture Overview

## All Files do the following
- Creates a List to store the completion time.
- Creates a list for Turnaround Time.
- Creates a list for Waiting Time.
- Obtains the Average Turnaround Time.
- Obtains the Average Waiting Time.
- Obtains the CPU Utilization through total burst time and total time.
- Identifies the Throughput of the complete process.

## Job Generation.py

This script generates a set of random processes, each with an arrival time and burst time, which are used as inputs for the scheduling algorithms.

## Multilevel Queue Scheduling.py

This script implements the Multilevel Queue Scheduling algorithm. It categorizes processes into different queues based on factors like priority or memory requirements and schedules them based on these categories.

## Priority Scheduling Non-Preemptive Algorithm.py

This script implements the Priority Scheduling algorithm without preemption. In this algorithm, processes are executed based on their priority. Higher priority processes are executed first, and once a process starts, it cannot be interrupted.

## Priority Scheduling Preemptive Algorithm.py

This script implements the Preemptive Priority Scheduling algorithm. Similar to the non-preemptive version, but the process with the highest priority can preempt a running process.

## Round Robin Algorithm.py

This script implements the Round Robin (RR) scheduling algorithm, where each process is given a fixed time slice (quantum). If a process does not finish in its assigned time slice, it is preempted and placed back in the queue.

## SJF Non-Preemptive Algorithm.py

This script implements the Shortest Job First (SJF) algorithm in its non-preemptive form. The process with the shortest burst time is executed next, and once a process starts, it cannot be interrupted.

## SJF Preemptive Algorithm.py

This script implements the Preemptive Shortest Job First (SJF) algorithm, also known as Shortest Remaining Time First (SRTF). The CPU selects the process with the shortest remaining burst time, and if a new process arrives with a shorter remaining burst time, it preempts the currently running process.

---

# How to Run

1. Clone the repository to your local machine.

```bash
    git clone https://github.com/AGCalixto/Algorithms
```

2. Naviggate to the project folder.

```bash
    cd Algorithms
```

3. Run the specific algorithm script using Python.

```bash
    python FCFS Algorithm.py
    python Round Robin Algorithm.py
    python SJF Non-Preemptive Algorithm.py
```

You can modify the process list in each script or use the Job Generation.py script to generate random processes for testing.

---

## Author 

Dennis Alejandro Guerra Calix -- AGCalixto
