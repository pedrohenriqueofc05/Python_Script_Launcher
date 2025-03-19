import os
import sys
import json
import subprocess
from ttkbootstrap import *
import ttkbootstrap as ttk

# Constants
ROW_LIMIT = 4  # Maximum number of rows for buttons in the window


def launch_app(command_dict: dict) -> None:
    """
    Launches the specified application based on the command provided.
    The command should be a dictionary containing the path to the script and any arguments.
    The script should be a Python script (.py) and should exist in the specified path.
    The function checks if the command is valid and if the script exists before launching it.
    If the script is launched successfully, it waits for the process to complete and checks the return code.
    Parameters:
        command_dict (dict): A dictionary containing the command data to be executed.
    """
    try:
        # Check if the command is a dictionary
        if not check_dict(command_dict):
            print("Error: The command is not formatted correctly.")
            return

        # Get the script path and arguments
        script_path = command_dict.get("path")
        if command_dict.get("args"):
            args = command_dict.get("args")
            if isinstance(args, list):
                args = " ".join(args)
            else:
                args = str(args)
            cmd = f"{script_path} {args}"
        else:
            cmd = script_path

        # Check if the script is a Python script
        if not script_path.endswith(".py"):
            print("Error: The script is not a Python script.")
            return

        # Check if the script exists
        if os.path.exists(script_path):
            if sys.platform == "win32":
                # Launch the application using subprocess
                process = subprocess.Popen(["python", cmd], shell=True)
            elif sys.platform == "linux":
                # Launch the application using subprocess
                process = subprocess.Popen(["python3", cmd], shell=True)
            elif sys.platform == "darwin":
                # Launch the application using subprocess
                process = subprocess.Popen(["python3", cmd], shell=True)
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
                return
        else:
            print(f"Error: The script '{script_path}' does not exist.")
            return

    except Exception as e:
        print(f"Error launching the application: {e}")


def check_dict(command_dict: dict) -> bool:
    """
    Checks if the command dictionary is formatted correctly.
    The command dictionary should contain the following keys:
        - "path": The path to the script to be executed.
        - "args": (Optional) A list of arguments to be passed to the script.
    Parameters:
        command_dict (dict): The command dictionary to be checked.
    Returns:
        bool: True if the command dictionary is formatted correctly, False otherwise.
    """
    if not isinstance(command_dict, dict):
        return False
    if "path" not in command_dict:
        return False
    if not isinstance(command_dict["path"], str):
        return False
    if "args" in command_dict and not isinstance(command_dict["args"], (str, list)):
        return False
    return True


def load_data_config(dir) -> dict:
    """
    Loads the configuration data from the config.json file.
    The config.json file should be located in the specified directory.
    Parameters:
        dir (str): The directory where the config.json file is located.
    Returns:
        dict: A dictionary containing the configuration data.
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


def create_button(
    row_index: int,
    column_index: int,
    root: ttk,
    title: str,
    command_dict: dict,
    width: int,
) -> None:
    """
    Creates a button in the specified row and column of the given root.
    Parameters:
        row_index (int): The row index for the button.
        column_index (int): The column index for the button.
        root (ttk): The parent widget where the button will be placed.
        title (str): The title of the button.
        command_dict (dict): A dictionary containing the command to be executed when the button is clicked.
        width (int): The width of the button.
    """
    button = ttk.Button(
        root, text=title, command=lambda: launch_app(command_dict), width=width
    )
    button.grid(row=row_index, column=column_index, padx=10, pady=10)


def create_window(data: dict) -> None:
    """
    Creates the main window and populates it with buttons based on the provided data.
    Parameters:
        data (dict): A dictionary containing the configuration data for the buttons.
    """
    # Create the main window
    root = ttk.Window(themename="darkly")
    root.title("Tools Launcher")

    # Set the button size and padding params to use to calculate the window size
    button_width = max(len(key) for key in data.keys()) * 10
    button_height = 30
    padding = 50

    # Initialize row and column indices
    row_index = 0
    column_index = 0

    # Calculate the number of rows and columns for the window size
    num_buttons = len(data)
    num_columns = 1 if num_buttons <= 4 else int((len(data) // 4))
    num_rows = num_buttons if num_buttons <= 4 else 4  # Calculate rows needed

    # Calculate the window size based on button size, padding, and the number of columns and rows
    window_width = num_columns * button_width + (num_columns + 1) * padding
    window_height = num_rows * button_height + (num_rows + 1) * padding

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    # Create a label for the title
    title_label = ttk.Label(root, text="Tools Launcher", font=("Arial", 24))
    title_label.pack(padx=10, pady=20)

    # Create a frame for the buttons
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    # Create buttons based on the data
    for button_title, command_dict in data.items():
        create_button(
            row_index,
            column_index,
            button_frame,
            button_title,
            command_dict,
            int(button_width / 10),
        )
        row_index += 1
        column_index += 1 if row_index >= 4 else 0
        # Reset row index if it exceeds 4
        if row_index == ROW_LIMIT:
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
