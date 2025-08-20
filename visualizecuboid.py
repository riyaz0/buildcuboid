
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


from build import calculate_cuboid_architecture

def visualize_cuboid_3d(cuboid_data):
 
    num_bricks = cuboid_data["num_bricks"]
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    x_bricks = np.arange(num_bricks["length"] + 1)
    y_bricks = np.arange(num_bricks["width"] + 1)
    z_bricks = np.arange(num_bricks["height"] + 1)
    

    for x in x_bricks:
        for y in y_bricks:
            ax.plot([x, x], [y, y], [0, num_bricks["height"]], color='b', alpha=0.1)

    # Plotting horizontal lines (along y-axis)
    for x in x_bricks:
        for z in z_bricks:
            ax.plot([x, x], [0, num_bricks["width"]], [z, z], color='b', alpha=0.1)
    
    # Plotting horizontal lines (along x-axis)
    for y in y_bricks:
        for z in z_bricks:
            ax.plot([0, num_bricks["length"]], [y, y], [z, z], color='b', alpha=0.1)

    # Set axis labels and plot title
    ax.set_xlabel('Length (25 bricks)')
    ax.set_ylabel('Width (20 bricks)')
    ax.set_zlabel('Height (20 bricks)')
    ax.set_title('3D Cuboid Visualization (10,000 Bricks)')

    # Set the plot limits to match the number of bricks
    ax.set_xlim(0, num_bricks["length"])
    ax.set_ylim(0, num_bricks["width"])
    ax.set_zlim(0, num_bricks["height"])

    plt.show()

def visualize_top_view(cuboid_data):
    """
    Visualizes the cuboid's top view using matplotlib.

    Args:
        cuboid_data (dict): Data from calculate_cuboid_architecture.
    """
    num_bricks = cuboid_data["num_bricks"]
    
    fig, ax = plt.subplots()
    ax.set_title('Top View')
    ax.set_xlabel('Length (25 bricks)')
    ax.set_ylabel('Width (20 bricks)')
    
    # Draw the grid
    ax.set_xticks(np.arange(0, num_bricks["length"] + 1, 1))
    ax.set_yticks(np.arange(0, num_bricks["width"] + 1, 1))
    ax.grid(True, which='both', color='gray', linestyle='-', linewidth=0.5)
    
    # Set limits to fit the grid
    ax.set_xlim(0, num_bricks["length"])
    ax.set_ylim(0, num_bricks["width"])
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def visualize_side_view(cuboid_data):
    """
    Visualizes the cuboid's side view using matplotlib.

    Args:
        cuboid_data (dict): Data from calculate_cuboid_architecture.
    """
    num_bricks = cuboid_data["num_bricks"]
    
    fig, ax = plt.subplots()
    ax.set_title('Side View')
    ax.set_xlabel('Length (25 bricks)')
    ax.set_ylabel('Height (20 bricks)')
    

    ax.set_xticks(np.arange(0, num_bricks["length"] + 1, 1))
    ax.set_yticks(np.arange(0, num_bricks["height"] + 1, 1))
    ax.grid(True, which='both', color='gray', linestyle='-', linewidth=0.5)
    
   
    ax.set_xlim(0, num_bricks["length"])
    ax.set_ylim(0, num_bricks["height"])
    ax.set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    total_bricks_count = 10000
    brick_dims = (200, 100, 100)  

 
    cuboid_data = calculate_cuboid_architecture(total_bricks_count, brick_dims)
    

    visualize_cuboid_3d(cuboid_data)
    visualize_top_view(cuboid_data)
    visualize_side_view(cuboid_data)
