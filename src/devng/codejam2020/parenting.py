#!/usr/bin/env python3
# coding: utf-8

from copy import deepcopy

# Checks if a solution shedule is valid for the given tasks
def check_solution(tasks, solution):
    if len(solution) != len(tasks):
        return False

    shedule_c = []
    shedule_j = []
    for i in range(len(tasks)):
        task = tasks[i]
        if solution[i] == "J" and can_add_task_shedule(task, shedule_j):
            shedule_j.append(task)
        elif solution[i] == "C" and can_add_task_shedule(task, shedule_c):
            shedule_c.append(task)
        else:
            return False
    return True


def is_shedule_possible(tasks):
    minutes_day = [0] * (60 * 24 + 1)
    for t in tasks:
        for i in range(t[0], t[1]):
            minutes_day[i] += 1
    for m in minutes_day:
        if m > 2:
            return False
    
    return True


# Input task array in the form: [(S0, E0, 0), (S1, E1, 1), ... , (Si, Ei, i)]
# returns a shedule string
def assign_tasks(org_tasks):
    if not is_shedule_possible(org_tasks):
        return "IMPOSSIBLE"

    # sort the tasks and implment a greedy search
    tasks = deepcopy(org_tasks)
    tasks.sort(key = lambda t: t[0])
    
    shedule_c = []
    shedule_j = []
    solution = ""
    for t in tasks:
        if can_add_task_shedule(t, shedule_j):
            solution += "J"
            shedule_j.append(t)
        elif can_add_task_shedule(t, shedule_c):
            solution += "C"
            shedule_c.append(t)
        else:
            # We should not be able to come here, but program defensively
            return "WTF"
    return rearrange_solution(solution, tasks)


# We need to re-arrange the solution to the original task order
# this function does that based on the original index stored in each task
def rearrange_solution(solution, tasks):
    final_solution = [""] * len(tasks)
    for i in range(len(solution)):
        t = tasks[i]
        ch = solution[i]
        final_solution[t[2]] = ch
    
    return "".join(final_solution)


# Returns True if the task can be added, False otherwise
def can_add_task_shedule(new_task, shedule):
    # https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
    def is_overlapping(x1, x2, y1, y2):
        return x1 < y2 and y1 < x2
    
    for task in shedule:
        if is_overlapping(task[0], task[1], new_task[0], new_task[1]):
            return False
    return True


def parse_tasks(lines):
    tasks = []
    for i in range(len(lines)):
        line = lines[i].strip()
        t = list(map(int, line.split()))
        # add the original task index, this is needed because we sort the array later
        # at the end however we need to know the original order
        t.append(i) 
        tasks.append(t)

    return tasks


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    num_cases = int(input()) # read a line with a single integer
    for i in range(1, num_cases + 1):
        case_size = int(input())
        lines = []
        for _ in range(case_size):
            lines.append(input())
            
        tasks = parse_tasks(lines)
        shedule = assign_tasks(tasks)
        print("Case #{}: {}".format(i, shedule))
