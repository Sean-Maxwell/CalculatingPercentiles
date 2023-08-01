import locale
import tkinter as tk
from tkinter import messagebox

def calculate_percentile(value, percentile):
    # Same implementation as before
    return (percentile / 100) * value

def calculate_and_display():
    input_value = entry_input_value.get()
    percentile = entry_percentile.get()

    try:
        input_value = float(input_value)
        percentile = float(percentile)
        result = calculate_percentile(input_value, percentile)

        if result.is_integer():
            formatted_result = locale.format_string("%d", result, grouping=True)
        else:
            formatted_result = locale.format_string("%.2f", result, grouping=True)

        output_label.config(text=f"The {percentile:.2f}% percentile of {input_value:.2f} is {formatted_result} €.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

def clear_entries():
    entry_input_value.delete(0, tk.END)
    entry_percentile.delete(0, tk.END)
    output_label.config(text="")

# Set the locale to use commas as the thousands separator
locale.setlocale(locale.LC_ALL, '')

# Create the main window
window = tk.Tk()
window.title("Percentile Calculator")

# Create input elements
input_label = tk.Label(window, text="Enter the value in euros:")
entry_input_value = tk.Entry(window)
input_label.pack()
entry_input_value.pack()

percentile_label = tk.Label(window, text="Enter the percentile (e.g., 1.1, 5, 10.5):")
entry_percentile = tk.Entry(window)
percentile_label.pack()
entry_percentile.pack()

# Create buttons for calculation and clearing
calculate_button = tk.Button(window, text="Calculate", command=calculate_and_display)
clear_button = tk.Button(window, text="Clear", command=clear_entries)
calculate_button.pack()
clear_button.pack()

# Create an output label to display the result
output_label = tk.Label(window, text="", font=("Helvetica", 12, "bold"))
output_label.pack()

# Start the GUI event loop
window.mainloop()
