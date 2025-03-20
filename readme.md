# Python Script Launcher

## Overview

The Python Script Launcher is a graphical tool designed to streamline the process of running Python scripts. It provides a user-friendly interface to manage and execute scripts with ease.

## Features

-   Intuitive graphical interface for script execution.
-   Cross-platform support (Windows, macOS, Linux).
-   Configurable script paths and arguments via `config.json`.
-   Automatic detection of missing or invalid scripts.
-   Supports as many or few scripts as entered into the JSON dictionary.
-   Window automatically adjusts to fit the number of scripts.
-   Configurable row limit for buttons via `config.json`.
-   Detailed logging of application events and errors to `debug.log`.
-   **"Always on Top"** toggle option to keep the launcher window above other windows. This option is saved when the toggle is adjusted.

## Usage (Source Version)

1. **Setup Configuration**:

    - Add your Python script paths, optional arguments, and configuration settings to the `config.json` file. Example structure:

        ```json
        {
            "config": {
                "ROW_LIMIT": 4,
                "ALWAYS": true
            },
            "scripts": {
                "Example Script 1": {
                    "path": "C:\\ExampleFolder\\ExampleScript.py",
                    "args": ["arg1", "arg2"]
                },
                "Example Script No Args": {
                    "path": "C:\\ExampleFolder\\ExampleScript.py"
                }
            }
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
    - Use the **"Always on Top"** checkbox to toggle whether the launcher window stays above other windows.

## Usage (Built Version)

1. **Setup Configuration**:

    - Add your Python script paths, optional arguments, and configuration settings to the `config.json` file. Example structure:

        ```json
        {
            "config": {
                "ROW_LIMIT": 4,
                "ALWAYS": true
            },
            "scripts": {
                "Example Script 1": {
                    "path": "C:\\ExampleFolder\\ExampleScript.py",
                    "args": ["arg1", "arg2"]
                },
                "Example Script No Args": {
                    "path": "C:\\ExampleFolder\\ExampleScript.py"
                }
            }
        }
        ```

    - Place the `config.json` file in the same directory as the built executable.

2. **Run the Launcher**:

    - Double-click the executable file (e.g., `python_script_launcher.exe`).

3. **Use the Interface**:
    - Select a script from the graphical interface and click the corresponding button to execute it.
    - Use the **"Always on Top"** checkbox to toggle whether the launcher window stays above other windows.

## Configuration

The `config.json` file is used to define the scripts and settings available in the launcher. Example structure:

```json
{
    "config": {
        "ROW_LIMIT": 4,
        "ALWAYS": true
    },
    "scripts": {
        "Example Script 1": {
            "path": "C:\\ExampleFolder\\ExampleScript.py",
            "args": ["arg1", "arg2"]
        },
        "Example Script No Args": {
            "path": "C:\\ExampleFolder\\ExampleScript.py"
        }
    }
}
```

-   Replace the paths with the absolute paths to your scripts.
-   Add optional arguments as a list under the `args` key.
-   Adjust the `ROW_LIMIT` value to control the maximum number of rows for buttons in the interface.
-   Set the `ALWAYS` value to `true` or `false` to control whether the launcher window starts in "Always on Top" mode.
-   Ensure the file is in the same directory as the launcher.

## Logging

-   All application events and errors are logged to a file named `debug.log` in the same directory as the launcher.
-   The log includes timestamps, line numbers, function names, and detailed error messages for easier debugging.

## Requirements

### Source Version

-   Python 3.x
-   `ttkbootstrap` library (install via `pip install ttkbootstrap`)

### Built Version

-   No additional dependencies. Ensure the `config.json` file is in the same directory as the executable.

## Notes

-   Ensure all script paths in `config.json` are valid.
-   The launcher automatically adjusts its interface based on the number of scripts configured and the `ROW_LIMIT` setting.
-   For troubleshooting, check the `debug.log` file for detailed error messages.

## Known Issues

-   No support for older versions of Python.
-   Scripts without a valid `path` key in `config.json` will not be executed.

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
-   For the source version, check the `debug.log` file for error messages.
-   For the built version, ensure all required scripts are accessible and valid.

## License

Under license via [MIT License](https://opensource.org/license/mit):

Copyright 2025 - Nicolas St-Amour

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
