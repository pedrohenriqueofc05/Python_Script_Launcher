import os
import sys
import json
import subprocess
from ttkbootstrap import *
import ttkbootstrap as ttk


def launch_app(script_path) -> None:
    """
    Launches the specified application based on the command provided.
    """
    try:
        # Check if the script exists
        if os.path.exists(script_path):
            if sys.platform == "win32":
                # Launch the application using subprocess
                process = subprocess.Popen(["python", script_path], shell=True)
            elif sys.platform == "linux":
                # Launch the application using subprocess
                process = subprocess.Popen(["python3", script_path], shell=True)
            elif sys.platform == "darwin":
                # Launch the application using subprocess
                process = subprocess.Popen(["python3", script_path], shell=True)
            else:
                print(f"Unsupported platform: {sys.platform}")
                return
            # Wait for the process to complete
            process.wait()
            # Check if the process was successful
            if process.returncode == 0:
                print(f"Successfully launched the application: {script_path}")
            else:
                print(f"Failed to launch the application: {script_path}")
        else:
            print(f"Error: The script '{script_path}' does not exist.")
    except Exception as e:
        print(f"Error launching the application: {e}")


def load_data_config(dir) -> dict:
    """
    Loads the configuration data from the config.json file.
    """
    try:
        with open(os.path.join(dir, "config.json"), "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: config.json file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from config.json.")
        return {}


def create_button(row_index, column_index, root, title, path, width) -> None:
    button = ttk.Button(root, text=title, command=lambda: launch_app(path), width=width)
    button.grid(row=row_index, column=column_index, padx=10, pady=10)


def create_window(data: dict) -> None:
    root = ttk.Window(themename="darkly")
    root.title("Tools Launcher")

    button_width = (
        max(len(key) for key in data.keys()) * 10
    )  # Calculate width based on the longest key
    button_height = 30  # Approximate height of a button in pixels
    padding = 50  # Padding around the buttons in pixels

    row_index = 0
    column_index = 0

    # Calculate the number of rows and columns
    num_buttons = len(data)
    num_columns = 1 if num_buttons <= 4 else int((len(data) // 4))
    num_rows = num_buttons if num_buttons <= 4 else 4  # Calculate rows needed

    # Calculate the window size
    window_width = num_columns * button_width + (num_columns + 1) * padding
    window_height = num_rows * button_height + (num_rows + 1) * padding

    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    # Create a label for the title
    title_label = ttk.Label(root, text="Tools Launcher", font=("Arial", 24))
    title_label.pack(padx=10, pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    for button_title, path in data.items():
        create_button(
            row_index,
            column_index,
            button_frame,
            button_title,
            path,
            int(button_width / 10),
        )
        row_index += 1
        column_index += 1 if row_index >= 4 else 0
        if row_index == 4:
            row_index = 0

    root.mainloop()


if __name__ == "__main__":
    # Set the current working directory to the script's directory
    script_path = sys.argv[0]
    if os.path.dirname(script_path):
        script_dir = os.path.dirname(script_path)
    else:
        script_dir = os.getcwd()

    # Load the configuration data
    data = load_data_config(script_dir)
    # Check if data is loaded successfully
    if not data:
        print("No data loaded. Exiting.")
        sys.exit(1)

    # Create and launch the main window
    create_window(data)
