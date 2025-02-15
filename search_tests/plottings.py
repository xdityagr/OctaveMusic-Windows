import numpy as np
import matplotlib.pyplot as plt

# Data for time taken (in seconds) for both methods
limits = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69])
time_v1 = np.array([6.90, 9.78, 8.03, 10.83, 12.99, 10.27, 12.34, 9.97, 10.61, 10.00, 10.10, 10.20, 11.35, 10.12, 10.14, 10.30, 9.85, 8.46, 7.21, 10.61, 10.42, 15.01, 14.68, 14.44, 9.17, 14.20, 14.75, 6.08, 7.75, 5.66, 4.36, 14.56, 8.14, 9.21, 12.21, 15.91, 14.93, 10.86, 15.02, 15.90, 13.27, 11.72, 21.29, 11.74, 11.73, 13.29, 22.42, 21.64, 11.24, 20.12])
time_v2 = np.array([3.04, 4.22, 4.26, 4.10, 4.10, 3.99, 4.18, 4.23, 4.24, 4.16, 4.27, 4.06, 4.23, 4.14, 4.21, 4.43, 4.43, 4.56, 4.23, 4.02, 5.05, 5.47, 5.58, 5.24, 5.67, 5.23, 5.32, 5.62, 5.64, 5.24, 5.51, 6.15, 7.35, 5.50, 5.87, 5.68, 5.12, 5.70, 5.91, 5.78, 6.22, 6.61, 7.46, 7.42, 7.74, 7.37, 8.19, 6.37, 7.51, 7.60])

# Calculate min, max, avg for both methods
min_v1 = np.min(time_v1)
max_v1 = np.max(time_v1)
avg_v1 = np.mean(time_v1)

min_v2 = np.min(time_v2)
max_v2 = np.max(time_v2)
avg_v2 = np.mean(time_v2)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(limits, time_v1, label='Grape Fetch V1', marker='o', color='b')
plt.plot(limits, time_v2, label='Grape Fetch V2', marker='o', color='g')
plt.xlabel('Limit')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken vs Limit for Grape Fetch V1 and V2')
plt.legend()
plt.grid(True)
plt.show()

min_v1, max_v1, avg_v1, min_v2, max_v2, avg_v2
