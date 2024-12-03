import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = '/filepath' 
data = pd.read_csv(file_path)

# Clean column names for better readability
data.columns = [col.strip() for col in data.columns]

# Define the lengths (starting from 45nm with 22.5nm increments)
num_lengths = len(data.columns) // 2  # Each length has 2 columns (X and Y)
lengths = [45 + i * 22.5 for i in range(num_lengths)]

# Define a colorblind-friendly palette and line styles
palette = sns.color_palette("colorblind", n_colors=num_lengths)
line_styles = ['-', '--', '-.', ':', '-', '--', '-.', ':', '-', '--', '-.']  # Repeated for variety

# Initialize the plot
plt.figure(figsize=(12, 6))

# Plot each length curve
for idx in range(num_lengths):
    x_col = data.columns[2 * idx]  # X-axis column
    y_col = data.columns[2 * idx + 1]  # Y-axis column
    x_data = pd.to_numeric(data[x_col], errors='coerce')  # Convert X-axis to numeric
    y_data = pd.to_numeric(data[y_col], errors='coerce')  # Convert Y-axis to numeric
    plt.plot(
        x_data, y_data,
        label=f"{lengths[idx]} nm",
        color=palette[idx],  # Color for distinction
        linestyle=line_styles[idx % len(line_styles)],  # Unique line styles
        linewidth=2  # Bold lines
    )

# Customize the plot
plt.title("$g_mr_o$ vs $g_m/I_d$ for Different Lengths", fontsize=14, weight='bold')
plt.xlabel("$g_m/I_d$", fontsize=12, weight='bold')
plt.ylabel("$g_mr_o$", fontsize=12, weight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Device Lengths", fontsize=10, title_fontsize=12, loc="upper left")
plt.tight_layout()

# Show the plot
plt.show()
