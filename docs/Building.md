# Building

## Prerequisites
Ensure you have the following tools installed on your system:

- **[Python 3.12.3](https://www.python.org/downloads/release/python-3123/)** (Other versions may work but are not guaranteed)
- **[Git](https://git-scm.com/)**

The project relies on these Python libraries:
- **[PySide6](https://doc.qt.io/qtforpython/gettingstarted.html#installation)**
- **[PyInstaller](https://pyinstaller.org/en/stable/)**

> **Tip:** I strongly recommend using a **virtual environment** to manage dependencies. The [PySide6 documentation](https://doc.qt.io/qtforpython/gettingstarted.html#installation) explains how to create one.

## Building from Source
This will generate an executable in the `dist` directory.
1. Clone the repository:
   ```bash
   git clone https://github.com/friedrichOsDev/save-file-control.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd save-file-control
   ```
3. Run the build script:
   ```bash
   python build.py
   ```
   > **Note:** Some systems might require `python3` instead of `python`.


