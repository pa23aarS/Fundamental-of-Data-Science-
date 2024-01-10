import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = "data3-2_-959907583.csv"
data = np.loadtxt(file_path, delimiter=",")

# Create histogram with a different color (e.g., green)
plt.hist(data, bins=20, density=True, alpha=0.7, color='green', edgecolor='black')

# Calculate mean annual salary
mean_salary = np.mean(data)

# Calculate another value X (replace this line with the actual calculation based on your requirements)
# For example, let's say X is the 75th percentile of the data
X = np.percentile(data, 75)

# Print W and X on the graph, including the student ID
plt.text(0.5, 0.95, f'Mean Salary (W~): ${mean_salary:.2f}', transform=plt.gca().transAxes, ha='center', va='center', backgroundcolor='w')
plt.text(0.5, 0.90, f'X: {X:.2f}', transform=plt.gca().transAxes, ha='center', va='center', backgroundcolor='w')
plt.text(0.5, 0.85, f'Student ID: 22092233', transform=plt.gca().transAxes, ha='center', va='center', backgroundcolor='w')

# Add labels and title
plt.xlabel('Annual Salary')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Annual Salary')

# Show legend
plt.legend(["Histogram"])

# Show the plot
plt.show()
