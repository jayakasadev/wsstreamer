import asyncio
import sys
from typing import List

# valid board
board1 = [
    [1, 2,3, 4, 5, 6, 7, 8, 9],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [3, 1, 2, 8, 4, 5, 9, 6, 7],
    [6, 9, 7, 3, 1, 2, 8, 4, 5],
    [8, 4, 5, 6, 9, 7, 3, 1, 2],
    [2, 3, 1, 5, 7, 4, 6, 9, 8],
    [9, 6, 8, 2, 3, 1, 5, 7, 4],
    [5, 7, 4, 9, 6, 8, 2, 3, 1],
]

# invalid boards
board2 = [
    [1, 2,3, 4, 5, 6, 7, 8, 9],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [3, 1, 2, 8, 4, 5, 9, 6, 7],
    [6, 9, 7, 3, 1, 1, 8, 4, 5],
    [8, 4, 5, 6, 9, 7, 3, 1, 2],
    [2, 3, 1, 5, 7, 4, 6, 9, 8],
    [9, 6, 8, 2, 3, 1, 5, 7, 4],
    [5, 7, 4, 9, 6, 8, 2, 3, 1],
]

board3 = [
    [1, 2,3, 4, 5, 6, 7, 8, 9],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [3, 1, 2, 8, 4, 5, 9, 6, 7],
    [6, 9, 7, 3, 1, 2, 8, 4, 5],
    [8, 4, 5, 6, 9, 7, 3, 1, 2],
    [2, 3, 1, 5, 7, 4, 6, 9, 8],
    [9, 6, 8, 2, 3, 1, 5, 7, 4],
    [5, 7, 4, 9, 6, 8, 2, 3, 5],
]

async def validate_row(row: List[int]) -> bool:
    """
    Method to validate the row

    Runtime: O(n)
    Space: O(n)
    Explanation:
    Given row has R elements, I iterate each element once.
    Also, creating the boolean list of size R will take O(R) space. In this case, R = 9.

    :param row: sudoku row
    :return: true if valid row else false
    """
    if len(row) > 9:
        return False
    validated = [False for _ in range(0, 10)]
    for i in row:
        if 1 > i > 9 or validated[i]:
            return False
        else:
            validated[i] = True
    return True


async def validate_board(board: List[List[int]]) -> bool:
    """
    Async Method to validate a completely filled out Sudoku board

    Runtime: O(N)
    Space: O(N)
    Explanation:
        Given a grid of size R x C, I am iterating each entry only once. No square is visited more than once even though
        I'm using nested for loops.
        I'm only O(RxC) space, which means I am not keeping duplicate values anywhere.


    :param board:
    :return:
    """
    cols = {}
    for row in board:
        # validate the current row first
        if await validate_row(row):
            for j in range(0, 8):
                if j in cols:
                    if row[j] in cols[j]:
                        return False
                    else:
                        # column size validation
                        if len(cols[j]) > 9:
                            return False
                        cols[j].add(row[j])
                else:
                    cols[j] = {row[j]}
        else:
            return False
    return True


async def main() -> int:
    # async functions, run multiple tests in parallel
    v1 = validate_board(board1)
    v2 = validate_board(board2)
    v3 = validate_board(board3)

    r1 = await v1
    r2 = await v2
    r3 = await v3
    print("Board1:", r1)
    print("Board2:", r2)
    print("Board3:", r3)

    return 0


if __name__ == '__main__':
    if sys.version_info[0] < 3 or sys.version_info[1] < 7:
        raise Exception("Must be using Python 3.7")
    sys.exit(asyncio.run(main()))
