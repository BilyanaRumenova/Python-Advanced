def read_input():
    jobs = list(map(int, input().split(", ")))
    job_index = int(input())
    return (jobs, job_index)


def get_min_cycles_for_job(jobs, job_index):
    sorted_jobs = sorted([(value, index) for (index, value) in enumerate(jobs)])
    cycles = 0
    for (value, index) in sorted_jobs:
        cycles += value
        if index == job_index:
            break

    return cycles


def print_result(min_cycles):
    print(min_cycles)


(jobs, job_index) = read_input()
min_cycles = get_min_cycles_for_job(jobs, job_index)
print_result(min_cycles)





