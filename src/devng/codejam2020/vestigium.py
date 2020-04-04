#!/usr/bin/env python3
# coding: utf-8


# gets the input mastrix as a string list and returns the case matrix as array of arrays
def parse_matrix_input(lines):
    case_matrix = []
    for i in range(len(lines)):
        line = lines[i].strip()
        case_matrix.append(list(map(int, line.split())))

    return case_matrix


def check_case(case_matrix):
    k = 0
    r = 0
    c = 0

    for i in range(len(case_matrix)):
        cur_num_row = {}
        cur_num_col = {}
        row_has_duplicates = False
        col_has_duplicates = False
        for j in range(len(case_matrix[i])):
            # we can check both rows and columns at the same time
            # since this is an NxN matrix
            num_row = case_matrix[i][j]
            num_col = case_matrix[j][i]
            
            if num_row not in cur_num_row:
                cur_num_row[num_row] = True
            else:
                row_has_duplicates = True

            if num_col not in cur_num_col:
                cur_num_col[num_col] = True
            else:
                col_has_duplicates = True
            
            if i == j:
                k += case_matrix[i][j]
        
        if row_has_duplicates:
            r += 1
        if col_has_duplicates:
            c += 1

    return k, r, c


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    num_cases = int(input()) # read a line with a single integer
    for i in range(1, num_cases + 1):
        case_size = int(input())
        lines = []
        for _ in range(case_size):
            lines.append(input())
            
        case = parse_matrix_input(lines)
        k, r, c = check_case(case)
        print("Case #{}: {} {} {}".format(i, k, r, c))

