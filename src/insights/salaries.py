from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        return max(
            int(job['max_salary'])
            for job in self.jobs_list
            if job['max_salary'] not in ("", "invalid")
        )

    def get_min_salary(self) -> int:
        return min(
            int(job['min_salary'])
            for job in self.jobs_list
            if job['min_salary'] not in ("", "invalid")
        )

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min = int(job['min_salary'])
            max = int(job['max_salary'])

            if min > max or min == "" or max == "":
                raise ValueError()
            if min <= int(salary) <= max:
                return True
            else:
                return False
        except (ValueError, TypeError, KeyError):
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
