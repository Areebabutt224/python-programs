from sklearn.linear_model import LinearRegression
import numpy as np

# Data: Study hours aur unke marks
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
marks = np.array([35, 40, 50, 55, 65, 70, 78, 85])

# Model banana aur train karna
model = LinearRegression()
model.fit(study_hours, marks)

# Naye hours ke liye prediction
hours = float(input("Enter study hours: "))
predicted_marks = model.predict([[hours]])

print("Predicted Marks:", predicted_marks[0])