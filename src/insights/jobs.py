import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file_path) -> List[Dict]:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                self.jobs_list.append(line)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        jobs = list()
        for job in self.jobs_list:
            jobs.append(job['job_type'])
        return list(set(jobs))

    def filter_by_multiple_criteria(self, jobs, filter_criteria) -> List[dict]:
        filtered_jobs = []
        for job in jobs:
            if job['industry'] == filter_criteria['industry'] and job['job_type'] == filter_criteria['job_type']:
                filtered_jobs.append(job)
        return filtered_jobs
