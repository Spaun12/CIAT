import pandas as pd
import matplotlib.pyplot as plt

# Initial data setup
data = {
    'Interval': ['Interval 1', 'Interval 2', 'Interval 3', 'Interval 4', 'Interval 5'],
    'MS Edge 1 (MB)': [460.908, None, None, None, None],
    'MS Edge 2 (MB)': [565.332, 558.560, 561.916, 557.800, 531.632],
    'MS Edge 3 (MB)': [709.896, 688.940, 702.584, 687.280, 620.788],
    'MS Edge 4 (MB)': [1233.024, 1224.120, 1222.648, 1214.680, 987.760],
    'Memory Compression (MB)': [3018.296, 3048.924, 3143.864, 3221.580, 3606.408],
    'WINWORD (MB)': [None, 469.692, 499.948, 501.612, 532.740]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Used direct assignment 
df['MS Edge 1 (MB)'] = df['MS Edge 1 (MB)'].ffill()
df['WINWORD (MB)'] = df['WINWORD (MB)'].ffill()

# Add Task Manager data to the DataFrame
df['Memory In Use (Compressed) (GB)'] = [24.3, 26.2, 26.1, 26.0, 25.3]
df['Available Memory (GB)'] = [6.8, 5.0, 4.9, 5.1, 5.8]

# Convert GB to MB for consistency in plotting
df['Memory In Use (Compressed) (MB)'] = df['Memory In Use (Compressed) (GB)'] * 1024
df['Available Memory (MB)'] = df['Available Memory (GB)'] * 1024

# Plotting
plt.figure(figsize=(12, 8))

# Plot each process memory usage
for column in df.columns[1:6]:  # Skip 'Interval' column and Task Manager data for line plotting
    plt.plot(df['Interval'], df[column], marker='o', label=column)

# Plot Task Manager data
plt.plot(df['Interval'], df['Memory In Use (Compressed) (MB)'], marker='s', linestyle='--', label='Memory In Use (Compressed)')
plt.plot(df['Interval'], df['Available Memory (MB)'], marker='^', linestyle='--', label='Available Memory')

plt.title('Memory Usage Overview Including System Data Over Time')
plt.xlabel('Collection Interval')
plt.ylabel('Memory Usage (MB)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Ensure the plot is displayed
plt.show()



