class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
       
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '.':
                    continue
                # Trick here is making 9 3X3 mini Grids with the index values of board
                # row//3 will be 0, 1, or 2 cols//3 = 0,1,2
                # Each sq[(0,0), (0,1)] etc is a mini grid
                # so squares[(0, 0)] will have 9 potential values
                # If any duplicates show then square is invalid and return false.
                if (board[row][col] in cols[col] or board[row][col] in rows[row] 
                or board[row][col] in squares[(row//3, col//3)]):
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True
