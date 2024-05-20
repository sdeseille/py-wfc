import random
import pprint

# Step 1: Define tiles and their adjacency rules
# Mountain => Land => Coast => Sea

tiles = {
    'M': {'left': ['M', 'L'], 'right': ['M', 'L'], 'top': ['M', 'L'], 'bottom': ['M', 'L']},
    'L': {'left': ['L', 'M'], 'right': ['L', 'M', 'C'], 'top': ['L', 'M'], 'bottom': ['L', 'M', 'C']},
    'C': {'left': ['B', 'C'], 'right': ['B', 'C'], 'top': ['C'], 'bottom': ['C']},
    'S': {'left': ['S', 'C'], 'right': ['S', 'C'], 'top': ['S', 'C'], 'bottom': ['S', 'C']}
}

# Step 2: Initialize grid
grid_width = 4
grid_height = 4
grid = [[list(tiles.keys())[:] for _ in range(grid_width)] for _ in range(grid_height)]
nextgrid = grid[:]
pprint.pprint(grid)


def calculate_entropy(x, y, min_entropy=float('inf')):
    print(min_entropy)
    min_cell = None
    entropy = len(grid[y][x])
    if 1 < entropy < min_entropy:
        min_entropy = entropy
        min_cell = (x, y)
    return min_cell

calculated_entropy=calculate_entropy(0,0)
if calculated_entropy:
    print(f"Entropy identified {calculated_entropy}")
    y, x = (calculated_entropy)
    possible_states = grid[y][x]
    chosen_state = random.choice(possible_states)
    print(f"Next tile type: {chosen_state}")
    nextgrid[y][x] = [chosen_state]


# Step 3: Propagate changes to neighbors
def propagate(nx, ny, direction):
    if 0 <= nx < grid_width and 0 <= ny < grid_height:
        neighbor_possible_states = grid[ny][nx]
        compatible_states = tiles[chosen_state][direction]
        grid[ny][nx] = [state for state in neighbor_possible_states if state in compatible_states]

propagate(x - 1, y, 'right')  # Left neighbor
propagate(x + 1, y, 'left')   # Right neighbor
propagate(x, y - 1, 'bottom') # Top neighbor
propagate(x, y + 1, 'top')    # Bottom neighbor

pprint.pprint(nextgrid)

# Step 7: Display the final grid
for row in nextgrid:
    print(' '.join(row[0] for row in row))
