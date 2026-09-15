import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [35, 40, 50, 55, 65, 70, 78]

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()