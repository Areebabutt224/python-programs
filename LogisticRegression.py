from sklearn.linear_model import LogisticRegression
import numpy as np

# Data: Study hours aur Pass(1)/Fail(0)
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
result = np.array([0, 0, 0, 1, 1, 1, 1, 1])   # 0 = Fail, 1 = Pass

# Model banana aur train karna
model = LogisticRegression()
model.fit(study_hours, result)

# Naye hours ke liye prediction
hours = float(input("Enter study hours: "))
prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")