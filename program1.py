class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # If the grid is empty, return 0
        if not grid:
            return 0
        
        # Number of rows and columns
        rows, cols = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Helper function for DFS
        def dfs(x, y):
            # If out of bounds or it's water, return
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 'W':
                return
            
            # Mark the current land cell as visited (turn it into water)
            grid[x][y] = 'W'
            
            # Explore all 4 directions (up, down, left, right)
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                dfs(new_x, new_y)
        
        # Count the number of islands
        island_count = 0
        
        # Traverse the grid
        for i in range(rows):
            for j in range(cols):
                # If we find a land cell, start a DFS and count a new island
                if grid[i][j] == 'L':
                    island_count += 1
                    dfs(i, j)  # Start DFS to mark all connected land cells
        
        return island_count

# Test cases
grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

# Creating a Solution object and calling the method
solution = Solution()
print(solution.getTotalIsles(grid1))  # Output: 1
print(solution.getTotalIsles(grid2))  # Output: 3
