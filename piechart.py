import matplotlib.pyplot as plt

activities = ["Study", "Sleep", "Play", "Other"]
hours = [4, 8, 2, 10]

plt.pie(hours, labels=activities)
plt.title("Daily Time Distribution")
plt.show()