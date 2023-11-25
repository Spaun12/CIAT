import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Sample data in the new CSV format
# In practice, this would be read from a CSV file
data_csv = """
DateTime,MemoryUsed,MemoryUsedNet,SwapUsed
2023-11-07 12:29:04,1896,1040,0
2023-11-07 12:34:04,1981,1103,0
2023-11-07 12:39:04,2257,1212,0
"""

# Use StringIO to simulate reading from a file
data = pd.read_csv(StringIO(data_csv))

# Convert DateTime to datetime object for plotting
data['DateTime'] = pd.to_datetime(data['DateTime'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['DateTime'], data['MemoryUsed'], label='Memory Used (MB)')
plt.plot(data['DateTime'], data['MemoryUsedNet'], label='Memory Used Net (MB)')
plt.plot(data['DateTime'], data['SwapUsed'], label='Swap Used (MB)')

# Adding labels and title
plt.xlabel('DateTime')
plt.ylabel('Memory Usage (MB)')
plt.title('Memory Usage Over Time')
plt.legend()

# Show the plot
plt.show()


