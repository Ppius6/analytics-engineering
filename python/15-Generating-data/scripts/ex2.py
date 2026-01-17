import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk(5_000)
rw.fill_walk()

# Plot the points in the walk
plt.style.use("classic")
fig, ax = plt.subplots()

point_numbers = range(rw.num_points)
ax.plot(
    rw.x_values,
    rw.y_values,
    linewidth=1,
    color="blue",
)

# Emphasize the first and last points
ax.plot(0, 0, marker="o", color="green", markersize=10)
ax.plot(rw.x_values[-1], rw.y_values[-1], marker="o", color="red", markersize=10)

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


ax.set_aspect("equal")

plt.show()
