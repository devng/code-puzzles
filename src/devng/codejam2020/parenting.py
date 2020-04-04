#!/usr/bin/env python3
# coding: utf-8

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


# Input task array in the form: [(S1, E1), (S2, E2), ...]
# returns a shedule string
def assign_tasks(tasks):
    # Bootstrap the process with assigning the first task to J
    # as we don't really care who takes the first tasks
    solution_stack = [("J", [], [tasks[0]])]

    while len(solution_stack) > 0:
        solution, shedule_c, shedule_j = solution_stack.pop()
        if len(solution) == len(tasks):
            return solution

        t = tasks[len(solution)]
        if can_add_task_shedule(t, shedule_j):
            new_solution = solution + "J"
            new_shedule_j = shedule_j.copy()
            new_shedule_j.append(t)
            solution_stack.append((new_solution, shedule_c, new_shedule_j))
        if can_add_task_shedule(t, shedule_c):
            new_solution = solution + "C"
            new_shedule_c = shedule_c.copy()
            new_shedule_c.append(t)
            solution_stack.append((new_solution, new_shedule_c, shedule_j))
    
    return "IMPOSSIBLE"


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
        tasks.append(list(map(int, line.split())))

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
