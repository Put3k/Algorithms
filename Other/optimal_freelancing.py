"""
You recently started freelance software development and have been offered a variety of job opportunities. Each job has a deadline, meaning there is no value in completing the work after the deadline. Additionally, each job has an associated payment representing the profit for completing that job. Given this information, write a function that returns the maximum profit that can be obtained in a 7-day period.
Each job will take 1 full day to complete, and the deadline will be given as the number of days left to complete the job. For example, if a job has a deadline of 1, then it can only be completed if it is the first job worked on. If a job has a deadline of 2, then it could be started on the first or second day.
Note: There is no requirement to complete all of the jobs. Only one job can be worked on at a time, meaning that in some scenarios it will be impossible to complete them all.
"""

def optimalFreelancing(jobs):

    result = 0

    jobs = sorted(jobs, key=lambda x: (-x['deadline'], -x['payment']))

    for day in range(7, 0, -1):
        highest_paid_modified = False
        highest_paid_job = {"deadline": 0, "payment": 0}
        for job in jobs:
            if job["deadline"] >= day and job["payment"] > highest_paid_job["payment"]:
                highest_paid_job = job
                highest_paid_modified = True

        if highest_paid_modified:
            result += highest_paid_job['payment']
            jobs.remove(highest_paid_job)

    return result


jobs = [
  {
    "deadline": 1,
    "payment": 1
  },
  {
    "deadline": 2,
    "payment": 1
  },
  {
    "deadline": 3,
    "payment": 1
  },
  {
    "deadline": 4,
    "payment": 1
  },
  {
    "deadline": 5,
    "payment": 1
  },
  {
    "deadline": 6,
    "payment": 1
  },
  {
    "deadline": 7,
    "payment": 1
  },
  {
    "deadline": 8,
    "payment": 1
  },
  {
    "deadline": 9,
    "payment": 1
  },
  {
    "deadline": 10,
    "payment": 1
  }
]

print(optimalFreelancing(jobs) == 7)

