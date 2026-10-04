import numpy as np
import matplotlib.pyplot as plt

# Vector Checks

def check_dependent(*vectors):
    M = np.array(vectors)

    rank = np.linalg.matrix_rank(M)
    
    if rank < len(vectors):
        print("Vectors are linearly dependent")
        return True
    else:
        print("Vectors are linearly independent")
        return False


# Vector Transformations

def rotate_clockwise(vector, degrees):
    vector = np.array(vector)

    theta = np.radians(-degrees)

    rotation_matrix = np.array([
        [np.cos(theta),  -np.sin(theta)],
        [np.sin(theta),   np.cos(theta)]
    ])

    return rotation_matrix @ vector

def rotate_counterclockwise(vector, degrees):
    vector = np.array(vector)

    theta = np.radians(degrees)

    rotation_matrix = np.array([
        [np.cos(theta),  -np.sin(theta)],
        [np.sin(theta),   np.cos(theta)]
    ])

    return rotation_matrix @ vector   

def shear(vector):
    rotation_matrix = np.array([
        [1, 1],
        [0, 1]
    ])

    return rotation_matrix @ vector

# Plotting

def plot_vector(ax, vector, color=None):

    if color is None:
        color = np.random.rand(3,)

    ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color)

def plot_span(vector1, vector2, num_iterations=3000, color=None):

    if color is None:
        color = np.random.rand(3,)

    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    
    fig, ax = plt.subplots()

    for i in range(num_iterations):
        a = np.random.uniform(-3, 3)
        b = np.random.uniform(-3, 3)

        point = a * vector1 + b * vector2
        ax.plot(point[0], point[1], ',', color=color, markersize=1)

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    plt.show()


# Vectors plotted
if __name__ == "__main__":
    fig, ax = plt.subplots()

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(-5, 6, 1))

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    ax.grid(True)


    plot_vector(ax, [1, 1])
    plot_vector(ax, [2, 3])
    plot_vector(ax, [3, 4])
    plot_vector(ax, [4, 5], 'green')


    plt.show()