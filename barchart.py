import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "Urdu"]
marks = [85, 90, 78, 88]

plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()