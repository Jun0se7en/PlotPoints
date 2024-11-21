import pandas as pd
import matplotlib.pyplot as plt

def plot_interactive(csv_file, x_column, y_column):
    # Load the CSV file
    data = pd.read_csv(csv_file)
    
    # Ensure the specified columns exist
    if x_column not in data.columns or y_column not in data.columns:
        print(f"Columns '{x_column}' or '{y_column}' not found in the CSV file.")
        return

    # Enable interactive mode
    plt.ion()
    
    fig, ax = plt.subplots()
    ax.set_title("Interactive Plot")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.grid(True)

    x = data[x_column]
    y = data[y_column]
    
    # Plot the data
    scatter = ax.scatter(x, y, c='blue', label='Points')
    ax.legend()
    
    plt.show(block=True)  # Keep the plot open for interaction
    plt.ioff()  # Disable interactive mode after closing

# Replace with your CSV file and the column names for x and y
csv_file_path = 'your_file.csv'
plot_interactive(csv_file_path, x_column='x', y_column='y')
