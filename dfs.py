import random
# @- black tiles, 1
# e- blue tiles, -1
# .- white tiles, 0

# Define grid size
grid_size = 32
num_blue_tiles = 52

def create_empty_grid():
    # Initialize grid with all white tiles ('.')
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    return grid

# Function to print the grid
def print_grid(grid, w_rows=None):
    if w_rows is None:
        w_rows = []  # Default to an empty list if no specific rows are provided

    for i in range(grid_size):
        # Determine the alternating character for the current row
        alt_char = 'w' if i in w_rows else '.'
        # Print the row with the additional columns
        print(alt_char + "." + ''.join(grid[i]) + "." + alt_char)
    print()

# Step 1: Place blue tiles ('e') sparsely across the grid
def place_blue_tiles(grid, num_blue_tiles=num_blue_tiles):
    count = 0
    while count < num_blue_tiles:
        x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        if grid[x][y] == '.':
            grid[x][y] = 'e'
            count += 1

# Step 2: Place black tiles ('@') adjacent to blue tiles
def place_black_tiles(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == 'e':
                shuffled_directions = random.sample(directions, len(directions))
                for dx, dy in shuffled_directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] == '.':
                        grid[nx][ny] = '@'
                        break

# Modified Step 3: Ensure black tiles ('@') have at least two adjacent blue tiles and can have more
def validate_black_tile_adjacency(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == '@':
                blue_count = 0
                # Randomly check directions to count adjacent blue tiles
                shuffled_directions = random.sample(directions, len(directions))
                for dx, dy in shuffled_directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] == 'e':
                        blue_count += 1
                while blue_count < 2:
                    for dx, dy in shuffled_directions:
                        nx, ny = x + dx, y + dy
                        if blue_count == 4:
                            break
                        if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] == '.':
                            grid[nx][ny] = 'e'
                            blue_count += 1
                            if blue_count >= 2 and random.random() < 0.5:
                                break

# Step 4: Ensure all blue tiles are connected by non-black paths
def validate_blue_connectivity(grid):
    visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]

    def dfs(x, y):
        if not (0 <= x < grid_size and 0 <= y < grid_size) or grid[x][y] == '@' or visited[x][y]:
            return
        visited[x][y] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    # Start DFS from the first blue tile
    start_found = False
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == 'e':
                dfs(x, y)
                start_found = True
                break
        if start_found:
            break

    # Check if all blue tiles are visited
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == 'e' and not visited[x][y]:
                return False
    return True

# Step 5: Correct the layout if needed
def correct_layout(grid):
    grid_i = grid.copy()
    # Ensure blue tiles are connected
    while not validate_blue_connectivity(grid_i):
        print("Re-validating and adjusting layout...")
        grid_i = create_empty_grid()  # Reset the grid
        place_blue_tiles(grid_i)  # Place initial blue tiles
        place_black_tiles(grid_i)  # Place black tiles
        validate_black_tile_adjacency(grid_i)
    
    return grid_i

# Main program
grid = create_empty_grid()
place_blue_tiles(grid)
place_black_tiles(grid)
validate_black_tile_adjacency(grid)
grid_i = correct_layout(grid)
print("Final Grid Layout:")
print_grid(grid_i, w_rows=[8, 16, 24])  # Specify the rows where 'w' should appear
