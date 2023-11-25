#!/bin/bash

# The file where we'll store our memory data
output_file="memory_data.txt"

# Function to append date and memory usage to the file
collect_memory_data() {
  date >> "$output_file"
  free -m >> "$output_file"
  echo "-------------------------------------------------" >> "$output_file"
}

# How many times to collect the data (12 times for 1 hour at 5-minute intervals)
count=12

# How long to wait between data collections (5 minutes)
interval=$((5 * 60))

# Collect the memory data
for ((i=1; i<=count; i++))
do
  collect_memory_data
  echo "Memory data collected $i time(s)."
  
  # Wait for the specified interval before next collection
  sleep "$interval"
done

echo "Data collection complete. Data saved to $output_file."
