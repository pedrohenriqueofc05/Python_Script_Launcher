# Python Script Launcher

## Overview

The Python Script Launcher is a graphical tool designed to streamline the process of running Python scripts. It provides a user-friendly interface to manage and execute scripts with ease.

## Features

-   Intuitive graphical interface for script execution.
-   Cross-platform support (Windows, macOS, Linux).
-   Configurable script paths via `config.json`.
-   Automatic detection of missing or invalid scripts.
-   Supports as many or few scripts as entered into JSON dict.
-   Window will adjust to fit.

## Usage (Source Version)

1. **Setup Configuration**:

    - Add your Python script paths to the `config.json` file. Example structure:
        ```json
        {
            "Script Name 1": "C:\\Path\\To\\Script1.py",
            "Script Name 2": "C:\\Path\\To\\Script2.py"
        }
        ```
    - Place the `config.json` file in the same directory as the `src/__init__.py` file.

2. **Run the Launcher**:

    - Open a terminal and navigate to the `src` directory.
    - Execute the following command:
        ```bash
        python __init__.py
        ```

3. **Use the Interface**:
    - Select a script from the graphical interface and click the corresponding button to execute it.

## Usage (Built Version)

1. **Setup Configuration**:

    - Add your Python script paths to the `config.json` file. Example structure:
        ```json
        {
            "Script Name 1": "C:\\Path\\To\\Script1.py",
            "Script Name 2": "C:\\Path\\To\\Script2.py"
        }
        ```
    - Place the `config.json` file in the same directory as the built executable.

2. **Run the Launcher**:

    - Double-click the executable file (e.g., `python_script_launcher.exe`).

3. **Use the Interface**:
    - Select a script from the graphical interface and click the corresponding button to execute it.

## Configuration

The `config.json` file is used to define the scripts available in the launcher. Example structure:

```json
{
    "Script Name 1": "C:\\Path\\To\\Script1.py",
    "Script Name 2": "C:\\Path\\To\\Script2.py"
}
```

-   Replace the paths with the absolute paths to your scripts.
-   Ensure the file is in the same directory as the launcher.

## Requirements

### Source Version

-   Python 3.x
-   `ttkbootstrap` library (install via `pip install ttkbootstrap`)

### Built Version

-   No additional dependencies. Ensure the `config.json` file is in the same directory as the executable.

## Notes

-   Ensure all script paths in `config.json` are valid.
-   The launcher automatically adjusts its interface based on the number of scripts configured.
-   For troubleshooting, check the console output (source version) or logs (if implemented in the built version).

## Building the Executable

To build the executable version of the launcher:

1. Install `PyInstaller`:

    ```bash
    pip install pyinstaller
    ```

2. Run the following command in the project directory:

    ```bash
    pyinstaller --onefile --noconsole src/__init__.py --name python_script_launcher
    ```

3. The built executable will be located in the `dist` directory.

## Troubleshooting

-   If the launcher fails to start, ensure the `config.json` file is correctly formatted and placed in the appropriate directory.
-   For the source version, check the terminal for error messages.
-   For the built version, ensure all required scripts are accessible and valid.

## License

Creative Commons NonCommercial 4.0 International (CC BY-NC 4.0)
