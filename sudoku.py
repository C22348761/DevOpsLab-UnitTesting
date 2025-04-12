def solve_sudoku(board):
    if len(board) != 81:
        raise ValueError("Board must have exactly 81 values")

    grid = board[:]
    given = [cell != 0 for cell in grid]
    box = []
    row = []
    column = []

    for i in range(0, 81, 9):
        row.append(list(range(i, i + 9)))
    for i in range(9):
        column.append(list(range(i, 81, 9)))
    box.append([0, 1, 2, 9, 10, 11, 18, 19, 20])
    box.append([3, 4, 5, 12, 13, 14, 21, 22, 23])
    box.append([6, 7, 8, 15, 16, 17, 24, 25, 26])
    box.append([27, 28, 29, 36, 37, 38, 45, 46, 47])
    box.append([30, 31, 32, 39, 40, 41, 48, 49, 50])
    box.append([33, 34, 35, 42, 43, 44, 51, 52, 53])
    box.append([54, 55, 56, 63, 64, 65, 72, 73, 74])
    box.append([57, 58, 59, 66, 67, 68, 75, 76, 77])
    box.append([60, 61, 62, 69, 70, 71, 78, 79, 80])

    def valid(n, pos):
        r = pos // 9
        c = pos % 9
        b = (r // 3) * 3 + (c // 3)

        for i in row[r]:
            if grid[i] == n:
                return False
        for i in column[c]:
            if grid[i] == n:
                return False
        for i in box[b]:
            if grid[i] == n:
                return False
        return True

    i = 0
    proceed = True
    while i < 81:
        if given[i]:
            i = i + 1 if proceed else i - 1
        else:
            n = grid[i]
            prev = n
            while n < 9:
                n += 1
                if valid(n, i):
                    grid[i] = n
                    proceed = True
                    break
            if grid[i] == prev:
                grid[i] = 0
                proceed = False
            i = i + 1 if proceed else i - 1
            if i < 0:
                raise ValueError("Unsolvable Sudoku puzzle")
    return grid
