#!/usr/bin/python3
import sys

# Check if there are more than one argument (excluding the script name)
if len(sys.argv) > 1:
    # Print the number of arguments provided (excluding the script name)
    print(f"Number of arguments: {len(sys.argv) - 1}")
    print("Arguments:")
    # Loop through the arguments starting from index 1 to skip the script name
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
else:
    # Print a message if no arguments are provided
    print("No arguments provided.")