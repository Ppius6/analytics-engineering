import plotly.express as px

from die import Die

# Create a D8 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()


# Make some rolls and store the results in a list
results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(10000)]

max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_results + 1)

frequencies = [results.count(value) for value in poss_results]

title = "Results of Rolling Three D6 10,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
