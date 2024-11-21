import time
import random

'''
Each user needs to perform 10 jobs, which include both print and scan tasks. 
Jobs have varying lengths based on the number of pages:
- Short Job: 1-5 pages
- Medium Job: 6-15 pages
- Large Job: 16-50 pages

Each page takes 1 second to process.
'''

# Part 1: Job Generator
# Initialization of the five users
User_Jobs = [[0]*10 for i in range(5)]
Users = {'P1': User_Jobs[0], 'P2': User_Jobs[1], 'P3': User_Jobs[2], 'P4': User_Jobs[3], 'P5': User_Jobs[4]}

# 10 Jobs for each user.
# Each job is randomly assigned to a printer or scanner.
# Random length for each job.

# Job Queue to store all the jobs.
Job_Queue = []

# Job Lengths
Short_Job = random.randint(1, 5)
Medium_Job = random.randint(6, 15)
Large_Job = random.randint(16, 50)
Jobs = [Short_Job, Medium_Job, Large_Job]

# Job Types (Can be either scan or print)
Job_Types = ['Print', 'Scan']

# To stack arrival times
cumulative_arrival_time = 0

# Assign each User 10 jobs with diverse arrival times (1 - 5).
for key, value in Users.items():
    # print(f'Generating jobs for {key}!')
    for i in range(0, 10):
        # The length of the job
        value[i] = random.choice(Jobs)

        # The job type
        job_type = random.choice(Job_Types)

        # The arrival time for each job
        arrival_time = random.randint(1, 5)
        # Stack the arrival times
        cumulative_arrival_time += arrival_time

        # The Job Details to add into the queue
        Job_Details = {'User': key, 'Job Type': job_type,
                       'Length': f'{value[i]} pages',
                       'Arrival Time': f'{cumulative_arrival_time} seconds'}

        # Add the jobs to the queue
        Job_Queue.append(Job_Details)

        # Print each job separately
        # print(f" User {key}: {job_type} Job {i+1}, {value[i]} pages, Arrival Time: {arrival_time} seconds")

'''
# Print the Job Queue
print('\n----------------J-O-B--L-I-S-T:-------------------- ')
for job in Job_Queue:
    print(f"User {job['User']}: {job['Job Type']} Job, {job['Length']}, Arrival Time: {job['Arrival Time']}")
'''


# Simulate job execution without synchronization and possible race conditions
def execute_jobs(job_queue):
    print("\nStarting Job Execution with Potential Race Conditions...\n")

    # Track pages left for each job
    jobs_in_progress = [{"User": job["User"],
                         "Job Type": job["Job Type"],
                         "Pages Left": int(job["Length"].split()[0]),
                         "Arrival Time": job["Arrival Time"]}
                        for job in job_queue]

    # Simulate the execution of jobs
    while jobs_in_progress:
        # Randomly pick a job from jobs_in_progress to simulate preemption
        current_job = random.choice(jobs_in_progress)

        # Simulate page-by-page execution
        user = current_job["User"]
        job_type = current_job["Job Type"]
        pages_left = current_job["Pages Left"]

        if pages_left > 0:
            print(f"User {user}: {job_type} Job, Processing Page. Pages Left: {pages_left}")
            # Simulate processing of a single page
            time.sleep(0.1)  # Short sleep to mimic work and allow context switch

            # Reduce pages left by 1
            current_job["Pages Left"] -= 1

            # Log status if there are race conditions
            if random.choice([True, False]):  # Randomly introduce inconsistency
                print(f"ERROR: Resource conflict detected! User {user} attempted to access {job_type} simultaneously.")

        # Remove completed jobs
        if current_job["Pages Left"] == 0:
            print(f"User {user}: {job_type} Job completed.\n")
            jobs_in_progress.remove(current_job)


# Example usage of execute_jobs
execute_jobs(Job_Queue)

