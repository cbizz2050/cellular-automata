# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
N = 100

# Initialize the grid with random values (0 or 1)
# 0 represents a dead cell, 1 represents a live cell
grid = np.random.randint(2, size=(N, N))

# Define the update function that will be called for each frame of the animation
def update(data):
    # Make the grid variable accessible inside the function
    global grid
    # Create a copy of the grid to hold the new state
    new_grid = grid.copy()
    # Iterate over each cell in the grid
    for i in range(N):
        for j in range(N):
            # Calculate the total number of live cells in the 8 neighboring cells
            # We use the modulo operator (%) with N to ensure that the edges of the grid wrap around
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                     grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            # Apply the rules of Life
            if grid[i, j]  == 1:
                # If a live cell has fewer than 2 or more than 3 live neighbors, it dies
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                # If a dead cell has exactly 3 live neighbors, it becomes a live cell
                if total == 3:
                    new_grid[i, j] = 1
    # Update the data of the matshow object to show the new state of the grid
    mat.set_data(new_grid)
    # Replace the old grid with the new grid
    grid = new_grid
    # Return the matshow object so that the animation function knows what to redraw
    return [mat]

# Create a new figure and axes object
fig, ax = plt.subplots()
# Create a new matshow object to visualize the grid
mat = ax.matshow(grid, cmap='viridis')
# Create a new animation object
# This object will call the update function for each frame, every 50 milliseconds
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)

# Display the animation
plt.show()
