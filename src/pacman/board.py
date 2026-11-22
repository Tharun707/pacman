class Board:

    def __init__(self,layout):
        self.grid = [list(row) for row in layout]

    def is_wall(self,row,col) -> bool:

        #checkig bound
        if row >= len(self.grid)  or row < 0:
            return True
        if col >= len(self.grid[0])  or col < 0:
            return True
        #checking for wall"#"
        return self.grid[row][col] == "#"

    def dots_remaining(self) -> int:
        count = 0
        for i in self.grid:
            count += i.count(".")
        return count



    

