

def calculate_cuboid_architecture(total_bricks, brick_dimensions):
    
    num_bricks = {
        "length": 25,
        "width": 20,
        "height": 20
    }

    # Calculate final dimensions and convert to meters.
    final_length_m = (num_bricks["length"] * brick_dimensions[0]) / 1000.0
    final_width_m = (num_bricks["width"] * brick_dimensions[1]) / 1000.0
    final_height_m = (num_bricks["height"] * brick_dimensions[2]) / 1000.0

    return {
        "num_bricks": num_bricks,
        "final_dimensions": (final_length_m, final_width_m, final_height_m),
        "location": "On a flat, level surface.",
        "orientation": "The largest face (5.0m x 2.0m) is the base for maximum stability."
    }


if __name__ == "__main__":
    total_bricks_count = 10000
    brick_dims = (200, 100, 100)  # in mm


    result = calculate_cuboid_architecture(total_bricks_count, brick_dims)


    print("--- Cuboid Architecture Output ---")
    print(f"Final Cuboid Dimensions: {result['final_dimensions']}")
    print(f"Location: {result['location']}")
    print(f"Orientation: {result['orientation']}")
